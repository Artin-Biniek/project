from enum import Enum

VERIFIABLE_CREDENTIAL = 'VerifiableCredential'
VERIFIABLE_PRESENTATION = 'VerifiablePresentation'
VC_SCHEMA = 'https://www.w3.org/ns/credentials/v2'
BIT_STRING_STATUS_URL = 'https://www.w3.org/ns/credentials/status#BitstringStatusListCredential'

with open('op.txt', 'r') as file:
    JSON_LD_SCHEMA = file.read()

required_attributes = {
    VERIFIABLE_CREDENTIAL: ["credentialSubject", "issuer"],
    "JsonSchema": ["id", "type", "jsonSchema"],
    "BitstringStatusList": ["id", "type", "statusPurpose", "encodedList", "ttl", "statusReference", "statusSize"],
    "BitstringStatusListEntry": ["id", "type", "statusPurpose", "statusListIndex", "statusListCredential"],
    "DataIntegrityProof": ["id", "type", "challenge", "created", "domain", "expires", "nonce", "previousProof",
                           "proofPurpose", "cryptosuite", "proofValue", "verificationMethod"],
    "cnf": ["kid", "jwk"],
    "credentialSchema": ["type", "id"],
    "credentialStatus": ["type"],
    "evidence": ["type"],
    "termsOfUse": ["type"],
    "issuer": ["id"],
    "proof": ["type"],
    "refreshService": ["id", "type"]
}


class Restriction(Enum):
    MustBeUrl = 1


special_reqs = {
    "credentialStatus": {
        "type": [Restriction.MustBeUrl]
    }
}
