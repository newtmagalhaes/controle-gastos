

def bootstrap_themes(request):
    return {
        # (value, label, icon)
        'BOOTSTRAP_THEMES': [
            ('light', 'Light', 'sun-fill'),
            ('dark', 'Dark', 'moon-stars-fill'),
            ('auto', 'Auto', 'circle-half'),
        ]
    }
