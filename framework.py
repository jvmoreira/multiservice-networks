import json
from lib.network_function_resolver import NetworkFunctionResolver
from lib.network_function_validator import NetworkFunctionValidator
from lib.network_function_script_resolver import NetworkFunctionScriptResolver

with open('framework.config.json', 'r') as config_file:
    config = json.load(config_file)

    try:
        network_function = NetworkFunctionResolver.resolve(config['function'])

        NetworkFunctionValidator.validate(network_function, config)

        script = NetworkFunctionScriptResolver.resolve(network_function, config)

        output_file = open('{}-nf.py'.format(config['function']), 'w')
        output_file.write(script)
        output_file.close()

    except Exception as err:
        print(err)
