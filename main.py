# import utility
# from  snowflake_con import get_snowflake_connection


# conn = get_snowflake_connection()
# cursor = conn.cursor()


# # function to save the backup files to sql
# def save_ddl_to_file(view_names,ddl_statements, filename='output.sql'):
#     with open(filename, 'w') as file:
#         file.write(f"-- Backup of {len(view_names)} views\n\n")
#         for view in view_names:
#             file.write(f"-- {view}\n")
#         for ddl in ddl_statements:
#             file.write(f"{ddl};\n\n") 


# def generate_bkp_scripts(view_names,bkp_file_name):
#     '''
#     This function is used to generate backup scripts so if i screw up this we will have all the view back up in no time
#     '''
#     ddl_statements = []
#     for view in view_names:
#         ddl_statements.append(utility.get_ddl(cursor,view))
    
#     save_ddl_to_file(view_names,ddl_statements,bkp_file_name)




# def extract_views_definition(env='DEV'):
#     dev_views = utility.get_bre_views(cursor,env)
#     print(f" the count of bre views are : {len(dev_views)}")
#     ddl_list = []
#     for view in dev_views:
#         ddl_list.append(utility.get_ddl(cursor,view))
#     return ddl_list


# def bre_views_modification(ddl_list):
#     modified_ddl_list = [ ]
#     for ddl in ddl_list:
#         modified_view = ddl.replace("BIC","BIC_RULEENGINE",1)
#         modified_view = modified_view.replace("BRE_","",1)
#         modified_ddl_list.append(modified_view)
#     return modified_ddl_list


# def Bre_views_complete_deployment():
#     '''
#     1. we will convert the extracted ddl list to modified list
#     2. use the view names list to delete all the views in the old domain space

#     '''

#     ddl_list = extract_views_definition('TST')
#     modified_ddl_list = bre_views_modification(ddl_list)


#     # execute the modifided ddl statements
#     for modified_view_ddl in modified_ddl_list:
#         print(f"Executing DDL: {modified_view_ddl[20:50]}...")
#         cursor.execute(modified_view_ddl)


# def De_views_complete_deployment():
#     '''
#     1. we will get the de_views from the utility
#     2. we will run the rename statements de_ to ''
#     '''

#     view_names = utility.get_de_views(cursor,'TST')
#     print(f" the count of de views are : {len(view_names)}")

#     for view in view_names:
#         new_view_name = view.replace("DE_","",1)
#         rename_statement = f"ALTER VIEW {view} RENAME TO {new_view_name}"
#         print(f"Renaming view: {view} to {new_view_name}")
#         cursor.execute(rename_statement)



# def views_functioning_test():
#     '''
#     This function is used to test the functioning of views
#     '''
#     view_names = utility.get_all_views(cursor,'DEV')
#     total_view_count = len(view_names)
#     views_test = 0
#     views_with_error = 0
#     print(f" Total views to test : {total_view_count}")
#     for view in view_names:
#         print(f"Testing view: {view}")
#         try:
#             cursor.execute(f"explain using tabular SELECT * FROM {view}")
#             views_test += 1
#         except Exception as e:
#             print(f"Error in view {view}: {e}")
#             views_with_error += 1
#     print(f"Total views tested successfully: {views_test}")
#     print(f"Total views with errors: {views_with_error}")


# # testing all views functioning
# views_functioning_test()


# # testing de views
# # De_views_complete_deployment()




   
# # clean up the old views
# # bre_views = utility.get_bre_views(cursor,'TST')
# # print(f" the count of bre views are : {len(bre_views)}")
# # utility.clean_up_views(cursor,bre_views)

# # Bre_views_complete_deployment()

# # ddl_list = extract_views_definition('TST')
# # modified_ddl_list = bre_views_modification(ddl_list)
# # print(modified_ddl_list[0])



# # dev_view_names = utility.get_all_views(cursor,'DEV')
# # generate_bkp_scripts(dev_view_names,'dev_bkp_scripts.sql')

# # tst_view_names = utility.get_all_views(cursor,'TST')
# # generate_bkp_scripts(tst_view_names,'tst_bkp_scripts.sql')