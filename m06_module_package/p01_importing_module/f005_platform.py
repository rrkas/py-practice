import platform

print(platform.platform(aliased=True, terse=True))
print(platform.platform(aliased=True, terse=False))
print(platform.platform(aliased=False, terse=True))
print(platform.platform(aliased=False, terse=False))

"""
Windows-10
Windows-10-10.0.22000-SP0
Windows-10
Windows-10-10.0.22000-SP0
"""

print(platform.processor()) # Intel64 Family 6 Model 140 Stepping 1, GenuineIntel
print(platform.machine())   # AMD64

print(platform.system()) # Windows
print(platform.version()) # 10.0.22000

print([platform.python_implementation(), platform.python_version_tuple()]) # ['CPython', ('3', '7', '0')]


