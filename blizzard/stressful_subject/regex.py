import re


def is_stressful(subj):
    """
        recoognise stressful subject
    """
    if subj.isupper() or subj.endswith('!!!'):
        return True

    red_patterns = (r'h+\W*e+\W*l+\W*p',
                    r'a+\W*s+\W*a+\W*p',
                    r'u+\W*r+\W*g+\W*e+\W*n+\W*t')

    return any([re.search(pattern, subj.lower()) for pattern in red_patterns])
