is_simple_core = False

if is_simple_core:
    from myPackage.core_simple import Variable
    from myPackage.core_simple import Function
    from myPackage.core_simple import using_config
    from myPackage.core_simple import no_grad
    from myPackage.core_simple import as_array
    from myPackage.core_simple import as_variable
    from myPackage.core_simple import setup_variable
else:
    from myPackage.core_complex import Variable
    from myPackage.core_complex import Function
    from myPackage.core_complex import using_config
    from myPackage.core_complex import no_grad
    from myPackage.core_complex import as_array
    from myPackage.core_complex import as_variable
    from myPackage.core_complex import setup_variable
    from myPackage.core_complex import Parameter
    from myPackage.layers import Layer
    from myPackage.models import Model

setup_variable()