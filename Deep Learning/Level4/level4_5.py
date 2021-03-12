if '__file__' in globals():
    import os, sys
    print('__file__ in globals at level4_5.py')
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))