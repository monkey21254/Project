is_simple_core = True

if is_simple_core:
    from Level2.core_simple import Variable
    from Level2.core_simple import Function
    from Level2.core_simple import using_config
    from Level2.core_simple import no_grad
    from Level2.core_simple import as_array
    from Level2.core_simple import as_variable
    from Level2.core_simple import setup_variable
else:
    pass
    
setup_variable()