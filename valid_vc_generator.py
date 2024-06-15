import datetime
import itertools
import json
import os
import random

from utils import VERIFIABLE_CREDENTIAL, required_attributes, JSON_LD_SCHEMA, VERIFIABLE_PRESENTATION, VC_SCHEMA


class ValidVCGenerator:
    def __init__(self):
        self.ignored_attrs = ['@protected', '@id', '@type']

    def generate_id_string(self):
        return 'http://1edtech.edu/credentials/3732'

    def generate_type_string(self):
        return 'BitstringStatusListEntry'

    def generate_basic_type(self, attr_schema):
        def generate_value(attr_type):
            if attr_type == '@id':
                return [self.generate_id_string(), {'id': self.generate_id_string()}]
            elif attr_type == 'http://www.w3.org/2001/XMLSchema#dateTime':
                return [datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')]

        if isinstance(attr_schema, str):
            return generate_value(attr_schema)
        return generate_value(attr_schema['@type'])

    def generate_attribute(self, attr_name, attr_schema):
        req_attributes_map = {}
        arbitrary_atts_map = {}

        if '@context' in attr_schema:
            if attr_name in required_attributes:
                req_atts = required_attributes[attr_name]
                for ra in req_atts:
                    req_attributes_map[ra] = self.generate_attribute(ra, attr_schema['@context'][ra])

            for key, value in attr_schema['@context'].items():
                if key in self.ignored_attrs:
                    continue
                if attr_name in required_attributes:
                    if key in required_attributes[attr_name]:
                        continue
                arbitrary_atts_map[key] = self.generate_attribute(key, attr_schema['@context'][key])
        else:
            if attr_name in required_attributes:
                req_atts = required_attributes[attr_name]
                if len(req_atts) == 1 and req_atts[0] == 'id':
                    return [self.generate_id_string()]
                for ra in req_atts:
                    if ra == 'id':
                        req_attributes_map['id'] = self.generate_id_string()
                    else:
                        req_attributes_map[ra] = self.generate_type_string()
                # for now, we consider if an attr without context has req attributes, it doesnt have arbitrary attributes
                return [req_attributes_map]
            else:
                return self.generate_basic_type(attr_schema)
        results = []
        required_combinations = list(itertools.product(*req_attributes_map.values()))
        arbitrary_attrs_choices = {}
        for key, values in arbitrary_atts_map.items():
            # arbitrary types are not supported yet
            if values is None:
                arbitrary_attrs_choices[key] = ['unknown']
                continue
            new_values = [v for v in values]
            # An arbitrary value may not be in the VC.
            new_values.append(None)
            arbitrary_attrs_choices[key] = new_values
        arb_combinations = list(itertools.product(*arbitrary_attrs_choices.values()))
        combined_keys_unique = list(req_attributes_map.keys()) + list(arbitrary_atts_map.keys())

        total_combinations = list(itertools.product(required_combinations, arb_combinations))
        flattened_combinations = [list(itertools.chain(*combination)) for combination in total_combinations]

        for c in flattened_combinations:
            results.append({})
            if attr_name == VERIFIABLE_CREDENTIAL or attr_name == VERIFIABLE_PRESENTATION:
                results[-1]['@context'] = [VC_SCHEMA]

            for i in range(len(c)):
                if c[i] is None:
                    continue
                results[-1][combined_keys_unique[i]] = c[i]
            if attr_name == VERIFIABLE_CREDENTIAL:
                results[-1]['type'] = VERIFIABLE_CREDENTIAL
            else:
                results[-1]['type'] = VERIFIABLE_PRESENTATION

        return results


generator = ValidVCGenerator()

json_ld_schema = json.loads(JSON_LD_SCHEMA)

results = generator.generate_attribute(VERIFIABLE_CREDENTIAL, json_ld_schema['@context'][VERIFIABLE_CREDENTIAL])

random_items = random.sample(results, 50)

folder = './generated_vcs/'

if not os.path.exists(folder):
    os.makedirs(folder)

for i in range(len(random_items)):
    with open(folder + str(i) + '.json', 'w') as file:
        file.write(json.dumps(random_items[i]))
