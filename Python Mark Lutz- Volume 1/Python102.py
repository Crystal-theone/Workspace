import json;
dictObject={1:2,3:"4",6:[1,2,3]};
print(dictObject);
jsEncoded=json.dumps(dictObject);
print(jsEncoded);
jdDecoded=json.loads(jsEncoded);
print(jdDecoded);
