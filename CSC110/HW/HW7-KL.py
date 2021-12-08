def has_no_e():
    with open("words.txt", "r") as infile:
        word_list = infile.readlines()
        no_e_list = []
        for i in range(len(word_list)):
            for j in range(len(word_list[i])):
                if word_list[i][j] != 'e':
                    contains_e = False
                else:
                    contains_e = True
                    break
            if not contains_e:
                no_e_list.append(word_list[i])
                print(word_list[i])
        percentage = 100 - ((len(no_e_list) / len(word_list)) * 100)
        print(str(percentage) + '%', 'of the words do not contain "e"')


has_no_e()
