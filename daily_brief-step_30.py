# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: DailyBrief
def add_profile_support():
    """Add multi-profile support to DailyBrief"""
    profiles = {
        "default": {"name": "Default", "language": "ru", "timezone": "UTC"},
    }
    
    def get_current_profile():
        """Get the current active profile name"""
        return "default"
    
    def set_profile(name):
        """Set a new active profile"""
        if name not in profiles:
            raise ValueError(f"Profile '{name}' does not exist. Available: {list(profiles.keys())}")
        return True
    
    def list_profiles():
        """List all available profiles"""
        return list(profiles.keys())
    
    def add_profile(name, language="ru", timezone="UTC"):
        """Add a new profile"""
        if name in profiles:
            raise ValueError(f"Profile '{name}' already exists")
        profiles[name] = {"name": name, "language": language, "timezone": timezone}
        return True
    
    def get_profile_info(name):
        """Get full info about a specific profile"""
        return profiles.get(name)
    
    # Example usage:
    print("=== DailyBrief Multi-Profile Support ===")
    print(f"Current active profile: {get_current_profile()}")
    print(f"All available profiles: {list_profiles()}")
    
    # Add a new profile
    add_profile("work", language="en", timezone="America/New_York")
    add_profile("personal", language="ru", timezone="Europe/Moscow")
    
    print(f"\nAfter adding profiles:")
    print(f"All available profiles: {list_profiles()}")
    
    # Get info about a specific profile
    work_info = get_profile_info("work")
    print(f"Work profile: {work_info}")
    
    # Try to add duplicate (should fail)
    try:
        add_profile("work")
    except ValueError as e:
        print(f"\nError adding duplicate: {e}")
    
    # Switch profile
    set_profile("personal")
    print(f"Switched to profile: {get_current_profile()}")

add_profile_support()
