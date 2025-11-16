## Localization Variables

What are the key localization variables in Linux, their purposes, and how does the localization hierarchy work?

---

**Primary Localization Variables:**

**LC_ADDRESS** - Postal address format

**LC_MONETARY** - Currency and monetary value format
```bash
LC_MONETARY=en_US.UTF-8    # $1,234.56
LC_MONETARY=de_DE.UTF-8    # 1.234,56 €
```

**LC_MEASUREMENT** - Measurement system
```bash
LC_MEASUREMENT=en_US.UTF-8    # Imperial (feet, miles)
LC_MEASUREMENT=en_GB.UTF-8    # Metric (meters, kilometers)
```

**TZ** - Time zone
```bash
export TZ=America/New_York
export TZ=Europe/Berlin
export TZ=UTC
```

**LANG** - Default locale for all LC_* variables
```bash
export LANG=en_US.UTF-8    # US English
export LANG=fr_FR.UTF-8    # French
```

**LC_ALL** - Override ALL locale settings (highest priority)
```bash
export LC_ALL=en_US.UTF-8
```

**Localization Hierarchy (priority order):**
```
LC_ALL (highest - overrides everything)
    ↓
Specific LC_* variables (LC_MONETARY, LC_TIME, etc.)
    ↓
LANG (default fallback)
```

**Configuration Location:**
- System-wide: `/etc/locale.conf`
- User-specific: `~/.bashrc` or `~/.bash_profile`

**Viewing Current Locale:**
```bash
locale                    # Show all locale settings
echo $LANG               # Show default locale
```

**Use Cases:**
- **LC_ALL:** Troubleshooting locale issues, forcing consistent locale
- **LANG:** Setting overall system language
- **Specific LC_*:** Fine-tuning individual categories
- **TZ:** Alternative to `timedatectl` for time zone management

**Best Practice:** Use LANG for general settings; use LC_ALL only for troubleshooting.

