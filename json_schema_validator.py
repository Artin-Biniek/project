from jsonschema import validate, ValidationError

schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Verifiable Credential",
    "type": "object",
    "properties": {
        "@context": {
            "type": "array",
            "items": {
                "anyOf": [
                    {
                        "type": "string",
                        "format": "uri"
                    },
                    {
                        "type": "object"
                    }
                ]
            }
        },
        "id": {
            "type": "string",
            "format": "uri"
        },
        "type": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "kid": {
            "type": "string",
            "format": "uri"
        },
        "iss": {
            "type": "string",
            "format": "uri"
        },
        "sub": {
            "type": "string",
            "format": "uri"
        },
        "jku": {
            "type": "string",
            "format": "uri"
        },
        "x5u": {
            "type": "string",
            "format": "uri"
        },
        "aud": {
            "type": "string",
            "format": "uri"
        },
        "exp": {
            "type": "integer",
            "minimum": 0
        },
        "nbf": {
            "type": "integer",
            "minimum": 0
        },
        "iat": {
            "type": "integer",
            "minimum": 0
        },
        "cnf": {
            "type": "object",
            "properties": {
                "kid": {
                    "type": "string",
                    "format": "uri"
                },
                "jwk": {
                    "type": "object"
                }
            },
            "required": ["kid", "jwk"]
        },
        "_sd_alg": {
            "type": "string"
        },
        "_sd": {
            "type": "string"
        },
        "digestSRI": {
            "type": "string"
        },
        "digestMultibase": {
            "type": "string"
        },
        "mediaType": {
            "type": "string"
        },
        "description": {
            "type": "string"
        },
        "name": {
            "type": "string"
        },
        "VerifiableCredential": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "string",
                    "format": "uri"
                },
                "type": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    }
                },
                "credentialSchema": {
                    "type": "string",
                    "format": "uri"
                },
                "credentialStatus": {
                    "type": "string",
                    "format": "uri"
                },
                "credentialSubject": {
                    "type": "string",
                    "format": "uri"
                },
                "description": {
                    "type": "string"
                },
                "evidence": {
                    "type": "string",
                    "format": "uri"
                },
                "validFrom": {
                    "type": "string",
                    "format": "date-time"
                },
                "validUntil": {
                    "type": "string",
                    "format": "date-time"
                },
                "issuer": {
                    "type": "string",
                    "format": "uri"
                },
                "name": {
                    "type": "string"
                },
                "proof": {
                    "type": "object"
                },
                "refreshService": {
                    "type": "string",
                    "format": "uri"
                },
                "termsOfUse": {
                    "type": "string",
                    "format": "uri"
                },
                "confidenceMethod": {
                    "type": "string",
                    "format": "uri"
                },
                "relatedResource": {
                    "type": "string",
                    "format": "uri"
                }
            },
            "required": ["id", "type", "credentialSubject", "issuer", "proof"]
        },
        "VerifiablePresentation": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "string",
                    "format": "uri"
                },
                "type": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    }
                },
                "holder": {
                    "type": "string",
                    "format": "uri"
                },
                "proof": {
                    "type": "object"
                },
                "verifiableCredential": {
                    "type": "array",
                    "items": {
                        "type": "object"
                    }
                },
                "termsOfUse": {
                    "type": "string",
                    "format": "uri"
                }
            },
            "required": ["id", "type", "holder", "proof"]
        },
        "JsonSchemaCredential": {
            "type": "string"
        },
        "JsonSchema": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "string",
                    "format": "uri"
                },
                "type": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    }
                },
                "jsonSchema": {
                    "type": "object"
                }
            },
            "required": ["id", "type", "jsonSchema"]
        },
        "BitstringStatusListCredential": {
            "type": "string"
        },
        "BitstringStatusList": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "string",
                    "format": "uri"
                },
                "type": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    }
                },
                "statusPurpose": {
                    "type": "string"
                },
                "encodedList": {
                    "type": "string"
                },
                "ttl": {
                    "type": "string"
                },
                "statusReference": {
                    "type": "string",
                    "format": "uri"
                },
                "statusSize": {
                    "type": "integer",
                    "minimum": 0
                },
                "statusMessage": {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "string",
                            "format": "uri"
                        },
                        "type": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            }
                        },
                        "status": {
                            "type": "string"
                        },
                        "message": {
                            "type": "string"
                        }
                    },
                    "required": ["id", "type", "status", "message"]
                }
            },
            "required": ["id", "type", "statusPurpose", "encodedList", "ttl", "statusReference", "statusSize"]
        },
        "BitstringStatusListEntry": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "string",
                    "format": "uri"
                },
                "type": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    }
                },
                "statusPurpose": {
                    "type": "string"
                },
                "statusListIndex": {
                    "type": "string"
                },
                "statusListCredential": {
                    "type": "string",
                    "format": "uri"
                }
            },
            "required": ["id", "type", "statusPurpose", "statusListIndex", "statusListCredential"]
        },
        "DataIntegrityProof": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "string",
                    "format": "uri"
                },
                "type": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    }
                },
                "challenge": {
                    "type": "string"
                },
                "created": {
                    "type": "string",
                    "format": "date-time"
                },
                "domain": {
                    "type": "string"
                },
                "expires": {
                    "type": "string",
                    "format": "date-time"
                },
                "nonce": {
                    "type": "string"
                },
                "previousProof": {
                    "type": "string",
                    "format": "uri"
                },
                "proofPurpose": {
                    "type": "string",
                    "enum": ["assertionMethod", "authentication", "capabilityInvocation", "capabilityDelegation",
                             "keyAgreement"]
                },
                "cryptosuite": {
                    "type": "string"
                },
                "proofValue": {
                    "type": "string"
                },
                "verificationMethod": {
                    "type": "string",
                    "format": "uri"
                }
            },
            "required": ["id", "type", "challenge", "created", "domain", "expires", "nonce", "previousProof",
                         "proofPurpose", "cryptosuite", "proofValue", "verificationMethod"]
        }
    },
    "required": ["@context", "type"]
}

data = {
    "@context": [
        "https://www.w3.org/ns/credentials/v2",
        "https://www.w3.org/ns/credentials/examples/v2"
    ],
    "type": [
        "VerifiableCredential"
    ],
    "issuer": "did:example:issuer",
    "credentialSubject": {
        "id": "did:example:subject"
    }
}

def validate_json_ld(data, schema):
    try:
        validate(instance=data, schema=schema)
        print("JSON-LD data is valid.")
    except ValidationError as e:
        print("JSON-LD data is invalid:", json_file)

validate_json_ld(data, schema)
