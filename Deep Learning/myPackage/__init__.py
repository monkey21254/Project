is_simple_core = True

if is_simple_core:
    from myPackage.core_simple import Variable
    from myPackage.core_simple import Function
    from myPackage.core_simple import using_config
    from myPackage.core_simple import no_grad
    from myPackage.core_simple import as_array
    from myPackage.core_simple import as_variable
    from myPackage.core_simple import setup_variable
else:
    pass
    
setup_variable()