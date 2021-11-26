# =============== module2 ===================
# import module1
# module1.print_m1()

# from module1 import print_m1
# print_m1()

# from module1 import print_m1 as pm1
# pm1()

# =============== module2 ===================
if __name__=="__main__":
    # print(__name__)
    # import module2
    # help(module2)
    # print("-------------------------------------------")

    # module doc
    # import module_doc
    # help(module_doc)
    # print("-------------------------------------------")
    # help(module_doc.add)

    # private doc
    import module_private
    print(module_private.fibo(10))
    print(module_private.rms([1, 2, 3, 4]))
    # print(module_private.__squared([1, 2, 3, 4]))
