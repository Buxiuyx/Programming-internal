#My Own Program
#Group Job Manager, can store people's detail.
#Set jobs, salary, work hours and work days for them.
#Calculate weekly salary


#Creating the first worker
jobs = {'Programming': 22.00, "Cleaning": 18.90, "Doing Nothing But Encourage": 10.00}
worker1 = {'First name': 'Ross', 'Last name': 'Zhong', 'Job1': 'Programming', "Job1_hours": 8.00, "Job2": "Cleaning",
           "Job2_hours": 1.00, "Work day per week": 6}
worker2 = {"First name": "Pine", "Last name": "Apple", 'Job1': "Doing Nothing But Encourage", "Job1_hours": 8.00,
           "Work day per week": 7}
workers = {'Worker1': worker1, "Worker2": worker2, }


#Define a function that add jobs and the salary for the job.
def adding_jobs():
    job_adding = input("Enter the job type you want to add").title().strip()
    while True:
        try:
            salary_adding = float(input('Please enter the hourly salary of "{}"'.format(job_adding)))
            new_job_adding = {job_adding: salary_adding}
            jobs.update(new_job_adding)
            print(jobs)
            break
        except ValueError:
            print("Please enter a number")
            keep = input("Do you want to keep adding the job?").strip().lower()
            if keep == "yes" or keep == "y":
                change_job = input("Do you want to change the job you want to add?").strip().lower
                if change_job == 'yes' or change_job == "y":
                    job_adding = input('Enter the job you want to add')
                else:
                    print("Roger that")
            else:
                break


#Define a function that view the workers details. (finished)
def viewing_workers():
    while True:
        function = input("""1, Workers' detail
2, Workers' salary
Enter 1 or 2, or enter exit to return""").strip().lower()
        if function == '1':
            workers_detail()
        elif function == '2':
            workers_salary()
        elif function == "exit":
            break
        else:
            print("That's not an option")

#define a function that shows the workers_details inside the function viewing_workers().(finished)
def workers_detail():
    while True:
        for worker, worker_detail in workers.items():
            print(worker, worker_detail["First name"], worker_detail["Last name"])
        choose = input("Who do you wanna look up? Enter the worker and his number or enter No or N to return.").capitalize().strip()
        if choose in workers.keys():
            print(workers[choose])
            change = input("Do you want to change his detail? Enter yes, y").strip().lower()
            if change == "y" or change == "yes":
                worker_detail_change(workers[choose])
            else:
                pass
        elif choose == "No" or choose == "N":
            break

        else:
            print("That's not an option")

#def a function inside workers_detail for changing details.(finished)
def worker_detail_change(detail):
    while True:
        change = input("What do you want to change? Enter 'First name', 'Last name', 'Job', 'Job hours', "
                       "'Work day per week' and so on").strip().capitalize()
        if change == "First name":
            detail_change = input("Please enter new first name").strip().capitalize()
            detail["First name"] = detail_change
        elif change == "Last name":
            detail_change = input("Please enter new last name").strip().capitalize()
            detail["Last name"] = detail_change
        elif change == "Job":
            for works in detail.keys():
                if "Job" in works:
                    print(detail[works])
            while True:
                detail_change = input("Enter new jobs").capitalize()
                if detail_change not in jobs:
                    print()
                    if "Job1" not in detail.keys():
                        new_time = input("Enter the job time")
                        new_job = {"Job3": detail_change, "Job3_hours": new_time}
                        detail.update(new_job)
                    elif "Job2" not in detail.keys():
                        new_time = input("Enter the job time")
                        new_job = {"Job2": detail_change, "Job2_hours": new_time}
                        detail.update(new_job)
                    elif "Job3" not in detail.keys():
                        new_time = input("Enter the job time")
                        new_job = {"Job3": detail_change, "Job3_hours": new_time}
                        detail.update(new_job)
                    else:
                        job_delete = input("Each worker can only have maximum of three jobs. Please enter a job1,"
                                           "job2 or job3 to delete the current job").capitalize().strip()
                        if job_delete == "Job1":
                            del detail["Job1"]
                            print("You have deleted Job1, please enter new job")
                        if job_delete == "Job2":
                            del detail["Job2"]
                            print("You have deleted Job2, please enter new job")
                        if job_delete =="Job3":
                            del detail["Job3"]
                            print("You have deleted Job3, please enter new job")
                        continue

                keep = input("Would you like to keep changing? yes, y to continue").lower().strip()
                if keep == "yes" or keep == "y":
                    pass
                else:
                    break
        elif change == "Jobhours":
            job = []
            for works in detail.keys():
                if "Job" in works:
                    print(detail[works])
                if "Job" in works and "hours" not in works:
                    job.append(detail[works])
            while True:
                choose = input("Please enter the job to change the work time").capitalize().strip()
                if choose == "Job1" or choose in job:
                    while True:
                        try:
                            new_time = float(input("Entre the new time"))
                            detail["Job1_hours"] = new_time
                            break
                        except ValueError:
                            print("Please enter a number")
                        except KeyError:
                            print("Job1 is not available")
                elif choose == "Job2" or choose in job:
                    while True:
                        try:
                            new_time = float(input("Entre the new time"))
                            detail["Job2_hours"] = new_time
                            break
                        except ValueError:
                            print("Please enter a number")
                        except KeyError:
                            print("Job2 is not available")
                elif choose == "Job3" or choose in job:
                    while True:
                        try:
                            new_time = float(input("Entre the new time"))
                            detail["Job3_hours"] = new_time
                            break
                        except ValueError:
                            print("Please enter a number")
                        except KeyError:
                            print("Job3 is not available")
                else:
                    print("The job is not in")
                keep = input("Do you want to keep changing? yes or y").strip().lower()
                if keep == "yes" or keep == "y":
                    pass
                else:
                    break
        elif change == "Workdayperweek":
            while True:
                try:
                    while True:
                        detail_change = int(input("Enter the new work day per week"))
                        if detail_change > 7 or detail_change <= 0:
                            print("Please enter a number between 0 and 7")
                        elif detail_change < 7 or detail_change > 0:
                            detail["Work day per week"] = detail_change
                            break
                    break
                except ValueError:
                    print("Please enter a whole number")


        else:
            break




#define a function that shows the salary of workers inside the function viewing_workers().(finished)
def workers_salary():
    daily_total_paid = 0.00
    weekly_total_paid = 0.00
    for worker, worker_detail in workers.items():
        weekly_salary = 0.00
        daily_salary = 0.00
        job1_daily_salary = 0.00
        job2_daily_salary = 0.00
        job3_daily_salary = 0.00
        job1 = worker_detail["Job1"]
        job1_charges = jobs[job1]
        job1_time = worker_detail["Job1_hours"]
        job1_daily_salary = job1_charges * job1_time
        daily_salary += job1_daily_salary
        try:
            job2 = worker_detail["Job2"]
            job2_charges = jobs[job2]
            job2_time = worker_detail["Job2_hours"]
            job2_daily_salary = job2_charges * job2_time
            daily_salary += job2_daily_salary
        except KeyError:
            pass
        try:
            job3 = worker_detail["Job3"]
            job3_charges = jobs[job3]
            job3_time = worker_detail["Job3_hours"]
            job3_daily_salary = job3_charges * job3_time
            daily_salary += job3_daily_salary
        except KeyError:
            pass
        weekly_salary = daily_salary * worker_detail["Work day per week"]
        print(worker, worker_detail["First name"], worker_detail["Last name"], "Daily salary: {:.2f}$"
              .format(daily_salary), "Weekly salary: {:.2f}$".format(weekly_salary))
        daily_total_paid += daily_salary
        weekly_total_paid += weekly_salary
    print("Daily total paid is {:.2f}$\nWeekly total paid is {:.2f}$".format(daily_total_paid, weekly_total_paid))



def menu():
    choose = int(input("Enter 1 to add jobs \n"
                       "Enter 2 to view workers details \n"
                       "Enter 0 to exit "))
    while True:
        try:
            if choose == 1 :
                adding_jobs()
            elif choose == 2:
                viewing_workers()
            else:
                print("please enter a number")
        except ValueError:
            print("please enter a number")

menu()