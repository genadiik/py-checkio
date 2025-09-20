def checkio(expression):
    brackets = {'{': '}', '[': ']', '(': ')'}
    checklist = []
    for c in expression:
        if c in brackets.values():
            if len(checklist) == 0 or checklist[-1] != c:
                return False
            else:
                del checklist[-1]
        if c in brackets.keys():
            checklist.append(brackets[c])
    return len(checklist) == 0
