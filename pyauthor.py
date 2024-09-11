import numpy as np

def assign_affiliation_number(author_table):
    affl_list = (author_table['affl_code']).to_string(index=False).split()
    affl_dict = dict.fromkeys(affl_list)
    num = 1
    for affl in affl_dict.keys():
        affl_dict[affl] = num
        num+=1
    return affl_dict

def mnras_auth_list(filepath, author_table, affl_table):
    author_table.sort_values(by=['author_no', 'secondname'], inplace=True)
    author_table.reset_index(inplace=True)
    affl_nums = assign_affiliation_number(author_table)
    auth_num = author_table.shape[0]
    with open(filepath, 'w') as f:
        if auth_num == 1:
            short_str = author_table['firstname'][0][0]+'. ' + author_table['secondname'][0]
        elif auth_num == 2:
            short_str = author_table['firstname'][0][0]+'. ' + author_table['secondname'][0] + ' and ' + author_table['firstname'][1][0] + author_table['secondname'][1]
        else:
            short_str = author_table['firstname'][0][0]+'. ' + author_table['secondname'][0] + ' et al.'
        f.write(r'\author['+short_str+r']'+r'{\parbox{\textwidth}{\Large')
        for i in np.arange(auth_num):
            if author_table['author_no'][i] == 1:
                email_str = r'\thanks{Email: ' + author_table['email'][i] + r'}'
            else:
                email_str = ''
            if isinstance(author_table['ORCID'][i], str) == True:
                orcidstr = r'\orcidlink{' + author_table['ORCID'][i] + r'}'
            else:
                orcidstr = ''
            affl_codes = author_table['affl_code'][i].split()
            affl_str = r'$^{'+str(affl_nums[affl_codes[0]])
            if len(affl_codes)>1:
                for j in np.arange(len(affl_codes))[1:]:
                    affl_str += ','+str(affl_nums[affl_codes[j]])
            affl_str += r'}$'
            f.write('\n' + author_table['name_str'][i] + affl_str + email_str + orcidstr + r',')
        f.write('\n' + r'}')
        f.write('\n' + r'\vspace{0.2cm}')
        f.write('\n' + r'\\')
        f.write('\n' + r'% List of institutions')

        affl_nums_r = dict(zip(affl_nums.values(),affl_nums.keys()))
        for i in affl_nums_r.keys():
            f.write('\n' + r'$^{' + str(i) + r'}$' + affl_table.loc[affl_table['affl_code']==affl_nums_r[i], 'affl_str'].iloc[0]+ r'\\')
        
        f.write('\n' + r'}')