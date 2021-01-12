import os , sys
if __name__ == "__main__": 
    for (root,dirs,files) in os.walk('.', topdown=True): 
        for file in files:
            #print('processing: ', file)
            new_name = file.replace('.markdown','.md')
            os.rename(os.path.join(root,file), os.path.join(root,new_name))
            if new_name.endswith('.md'):
                with open(os.path.join(root,new_name), 'r+') as f:
                    #print('opening: ', new_name)
                    read_data = f.readlines()
                    #print('reading:', read_data)
                    write_data = read_data.copy()
                    index_to_be_deleted = []
                    toc_sticky = False
                    for index, line in enumerate(read_data):
                        if line.startswith('layout'):
                            write_data[index] = line.replace('post','single')
                        if line.startswith('modified'):
                            write_data[index] = line.replace('modified','last_modified_at')
                        if line.startswith('comments'):
                            index_to_be_deleted.append(index)
                        if line.startswith('image:'):
                            index_to_be_deleted.append(index)
                        if line.startswith('toc: true'):
                        	print('toc: ', new_name)
                        if 'feature:' in line:
                            index_to_be_deleted.append(index)
                        if 'credit:' in line:
                            index_to_be_deleted.append(index)
                        if 'creditlink:' in line:
                           index_to_be_deleted.append(index)
                        if '_toc.html' in line:
                            index_to_be_deleted.append(index)
                            toc_sticky = True
                            print('toc:', new_name)
                    #print(index_to_be_deleted)
                    for index in sorted(index_to_be_deleted, reverse = True):
                        #print('delete: ', write_data[index])
                        del write_data[index]
                    if toc_sticky:
                        write_data.insert(2,'toc_sticky: true\n')
                    #print(write_data)
                    f.seek(0)
                    f.truncate()
                    f.writelines(write_data)

