from pathlib import Path
import shutil


def wait_for_any_key(message: str = "Press any key to continue...") -> None:
    print(message)
    try:
        import msvcrt

        msvcrt.getch()
    except ImportError:
        input()


def prompt_yes_no(message: str) -> bool:
    while True:
        response = input(f"{message} ").strip().lower()
        if response in {"y", "yes"}:
            return True
        if response in {"n", "no"}:
            return False
        print("Please enter Y or N.")


def require_path_exists(path: Path, description: str) -> None:
    if not path.exists():
        raise FileNotFoundError(f"Required {description} was not found: {path}")


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    exe_path = base_dir / "ZenlessZoneZero.exe"
    data_dir = base_dir / "ZenlessZoneZero_Data"

    if not exe_path.is_file() or not data_dir.is_dir():
        print("Please place this script within ZenlessZoneZero's install folder.")
        print("(Example: D:\\SteamLibrary\\steamapps\\common\\Zenless Zone Zero\\games\\ZenlessZoneZero Game)")
        wait_for_any_key("Press any key to close...")
        return

    persistent_audio_dir = data_dir / "Persistent" / "Audio"
    persistent_version_file = data_dir / "Persistent" / "audio_version_persist"
    streaming_audio_dir = data_dir / "StreamingAssets" / "Audio"
    streaming_version_file = data_dir / "StreamingAssets" / "audio_version"

    if prompt_yes_no("Is ZZZ downloading files at login every time and resetting your audio mods? [Y/N]"):
        if prompt_yes_no("Fixing this will require we delete your audio files and have you manually reverify the game. Is this fine? [Y/N]"):
            if persistent_audio_dir.exists():
                shutil.rmtree(persistent_audio_dir)
            if streaming_audio_dir.exists():
                shutil.rmtree(streaming_audio_dir)
            print ("")
            print(
                "Deleted ZenlessZoneZeroe's Audio files. Please verify the game's files, "
                "run the game *TWICE*. The first run will download any further missing files "
                "(event audio). The second run should login normally."
            )
            print ("")
            wait_for_any_key("Press any key when you are done...")

    require_path_exists(persistent_audio_dir, "folder")
    require_path_exists(persistent_version_file, "file")
    require_path_exists(streaming_audio_dir, "folder")
    require_path_exists(streaming_version_file, "file")

    persistent_backup_audio_dir = data_dir / "Persistent-bak" / "Audio"
    persistent_backup_version_file = data_dir / "Persistent-bak" / "audio_version_persist"
    streaming_backup_audio_dir = data_dir / "StreamingAssets-bak" / "Audio"
    streaming_backup_version_file = data_dir / "StreamingAssets-bak" / "audio_version"

    print("Backing up persistent audio files...")
    shutil.copytree(persistent_audio_dir, persistent_backup_audio_dir, dirs_exist_ok=True)
    persistent_backup_version_file.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(persistent_version_file, persistent_backup_version_file)

    print("Backing up streaming audio files...")
    shutil.copytree(streaming_audio_dir, streaming_backup_audio_dir, dirs_exist_ok=True)
    streaming_backup_version_file.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(streaming_version_file, streaming_backup_version_file)

    print("Copying persistent audio to streaming audio...")
    shutil.copy2(persistent_version_file, streaming_version_file)
    shutil.copytree(persistent_audio_dir, streaming_audio_dir, dirs_exist_ok=True)

    print("")

    print(
        "Task complete. Run ZZZ, let it download any mismatched files (should be < 300Mb). "
        "Once its done verifying the files, relaunch the game to make sure it is loading "
        "without downloading any files. NOW you can try your audio mods."
    )

    print("")

    print(
        "(WARNING  - DO NOT let XXAR or ZZAR try to fix anything if you are prompted to do so. "
        "Doing so will nuke some files the game is looking for, breaking this fix.)"
    )

    print("")
    print("")
    wait_for_any_key("Press any key to close...")


if __name__ == "__main__":
    main()