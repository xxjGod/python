# from pydantic import json
import json

print(hasattr(json, "dumps"))

print(getattr(json, "__path__"))
print(dir(map))
print(dir(json))

dumps = getattr(json, "dumps")
print(dumps({"name": "xxj"}))
print(isinstance("python", str))

print(callable(str))

# print(help(json))
# print(json.__doc__)

print(json.__name__)
print(json.__file__)
print("##################")
print(json.__dict__)