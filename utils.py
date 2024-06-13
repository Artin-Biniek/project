import json
import os

import validators
from dateutil import parser

VERIFIABLE_CREDENTIAL = 'VerifiableCredential'
VERIFIABLE_PRESENTATION = 'VerifiablePresentation'
VC_SCHEMA = ''

text=input("Enter a)V2.0 or b)V1.1: ")
if text=="a":
    with open('op.txt', 'r') as file:
        JSON_LD_SCHEMA = file.read()
    VC_SCHEMA = 'https://www.w3.org/ns/credentials/v2'
    dir = './tests/input/'
    datetime_type='http://www.w3.org/2001/XMLSchema#dateTime'
if text=="b":
    with open('v1.txt', 'r') as file:
        JSON_LD_SCHEMA = file.read()
    VC_SCHEMA = 'https://www.w3.org/2018/credentials/v1'
    datetime_type='xsd:dateTime'
    dir = './vc-data-model-1.0/input/'

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

from enum import Enum


class Restriction(Enum):
    MustBeUrl = 1


special_reqs = {
    "credentialStatus": {
        "type": [Restriction.MustBeUrl]
    }
}