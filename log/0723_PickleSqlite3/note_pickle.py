import pickle

# serialize object as file
pickle.dump(obj, file, protocol=None, *, fix_imports=True)

# serialize object as byte object(d)
dump = pickle.dumps(obj, protocol=None, *, fix_imports=True)

# recreate objects from file
obj = pickle.load(file, *, fix_imports=True, encoding="ASCII", errors="strict")

# recreate objects from object
obj = pickle.loads(bytes_object, *, fix_imports=True, encoding="ASCII", errors="strict")
