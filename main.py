#My Own Program
#Group Job Manager, can store people's detail.
#Set jobs, salary, work hours and work days for them.
#Calculate weekly salary


#Creating the first worker
jobs = {'Programming': 22.00, "Cleaning": 18.90, "Doing Nothing": 1.00}
worker1 = {'First name': 'Ross', 'Last name': 'Zhong', 'Job1': 'Programming', "Job1_hours": 8.00, "Job2": "Cleaning",
           "Job2_hours": 1.00, "Work day per week": 6}
worker2 = {}
worker3 = {}
worker4 = {}
worker5 = {}
worker6 = {}
worker7 = {}
worker8 = {}
worker9 = {}
worker10 = {}
workers = {'Worker1': worker1, "Worker2": worker2, "Worker3": worker3, "Worker4": worker4, "Worker5": worker5,
           "Worker6": worker6, "Worker7": worker7, "Worker8": worker8, "Worker9": worker9, "Worker10": worker10}


#Define a function that add jobs and the salary for the job.
def adding_jobs():
    for job, salary in jobs.items():
        print("{}, \n{}$ per hour\n".format(job, salary))
    job_adding = input("Enter the job type you want to add, or enter no to exit").title().strip()
    if job_adding != "No" and job_adding != "N":
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
                        pass
                else:
                    break
    else:
        print("")

def deleting_jobs():
    while True:
        for job, salary in jobs.items():
            print("{}, \n${} per hour\n".format(job, salary))
        job_deleting = input("What job you wanna delete").title()
        if job_deleting in jobs.keys():
            jobs.pop(job_deleting)
        else:
            print("Sorry,that's not in the job list")
        keep = input("Do you want to keep deleting? Enter yes or no").title().strip()
        if keep == "Yes" or keep == "Y":
            pass
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
            if "First name" in worker_detail.keys() and "Last name" in worker_detail.keys():
                print(worker, worker_detail["First name"], worker_detail["Last name"])
            else:
                pass
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
                    addtolist = input("{} is not in the list. "
                                      "Would you like to add it to jobs list? Enter yes".format(detail_change)).strip().title()
                    if addtolist == "Yes" or addtolist == "Y":
                        while True:
                            print("You are adding job: ", detail_change)
                            try:
                                salary = int(input("Please enter the salary for it, or enter '0' to exit"))
                                if salary == 0:
                                    break
                                else:
                                    jobs[detail_change] = salary
                                    break
                            except ValueError:
                                print("That's not a number")
                        add = input("Would you like to add the job to the member's detail?").strip().title()
                        if add =="Yes" or add == "Y":
                            if "Job1" not in detail.keys():
                                new_time = input("Enter the job time")
                                new_job = {"Job1": detail_change, "Job1_hours": new_time}
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
                                job_delete = input(
                                    "Each worker can only have maximum of three jobs. Please enter a job1,"
                                    "job2 or job3 to delete the current job").capitalize().strip()
                                if job_delete == "Job1":
                                    del detail["Job1"]
                                    print("You have deleted Job1, please enter new job")
                                if job_delete == "Job2":
                                    del detail["Job2"]
                                    print("You have deleted Job2, please enter new job")
                                if job_delete == "Job3":
                                    del detail["Job3"]
                                    print("You have deleted Job3, please enter new job")
                                continue

                        keep = input("Would you like to keep changing? yes, y to continue").lower().strip()
                        if keep == "yes" or keep == "y":
                            pass
                        else:
                            break
                else:
                    if "Job1" not in detail.keys():
                        new_time = input("Enter the job time")
                        new_job = {"Job1": detail_change, "Job1_hours": new_time}
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
        elif change == "Work day per week":
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

#def a function adding workers
def adding_worker():
    while True:
        new_worker = input("Please enter new worker's First name, or enter no to exit").title().strip()
        if new_worker != "No" and new_worker != "N":
            for worker in workers.values():
                if len(worker) == 0:
                    add = {"First name": new_worker, "Last name": "", "Job1": "", "Job1_hours": 0, "Work day per week": 0}
                    worker.update(add)
                    lastname = input("Please enter new worker's last name?").title().strip()
                    worker["Last name"] = lastname
                    change = input("Would you like to change the new worker's detail? Enter yes to keep").strip().title()
                    if change == "Yes" or change == "Y":
                        worker_detail_change(worker)
                        break
                    else:
                        break
                else:
                    pass
        break


def deleting_workers():
    while True:
        for num, worker in workers.items():
            if "First name" in worker.keys() and "Last name" in worker.keys():
                print(num, worker["First name"], worker["Last name"])
        deleted_worker = input("Please enter the worker's LAST name to delete, or enter No to exit").strip().title()
        for worker in workers.values():
            try:
                if deleted_worker == worker["Last name"]:
                    list = []
                    for keys, values in worker.items():
                        list.append(keys)
                    for keys in list:
                        if keys in worker.keys():
                            del worker[keys]
                else:
                    pass
            except KeyError:
                pass
        keep = input("Would you like to keep deleting? Enter Yes to keep").strip().title()
        if keep == "Yes" or keep == "Y":
            pass
        else:
            break

#define a function that shows the salary of workers inside the function viewing_workers().(finished)
def workers_salary():
    daily_total_paid = 0.00
    weekly_total_paid = 0.00
    weekly_salary = 0.00
    daily_salary = 0.00
    job1_daily_salary = 0.00
    job2_daily_salary = 0.00
    job3_daily_salary = 0.00
    for worker, worker_detail in workers.items():
        if "Job1" in worker_detail:
            job1 = worker_detail['Job1']
            job1_charges = jobs[job1]
            job1_time = worker_detail["Job1_hours"]
            job1_daily_salary = job1_charges * job1_time
            daily_salary += job1_daily_salary
        else:
            pass
        if "Job2" in worker_detail:
            job2 = worker_detail["Job2"]
            job2_charges = jobs[job2]
            job2_time = worker_detail["Job2_hours"]
            job2_daily_salary = job2_charges * job2_time
            daily_salary += job2_daily_salary
        else:
            pass
        if "Job3" in worker_detail:
            job3 = worker_detail["Job3"]
            job3_charges = jobs[job3]
            job3_time = worker_detail["Job3_hours"]
            job3_daily_salary = job3_charges * job3_time
            daily_salary += job3_daily_salary
        else:
            pass
        if "Work day per week" in worker_detail:
            weekly_salary = daily_salary * worker_detail["Work day per week"]
            print(worker, worker_detail["First name"], worker_detail["Last name"], "Daily salary: {:.2f}$"
                  .format(daily_salary), "Weekly salary: {:.2f}$\n".format(weekly_salary))
        else:
            pass
    daily_total_paid += daily_salary
    weekly_total_paid += weekly_salary
    print("Daily total paid is {:.2f}$\nWeekly total paid is {:.2f}$".format(daily_total_paid, weekly_total_paid))



def menu():
    while True:
        try:
            choose = int(input("Enter 1 to add jobs \n"
                               "Enter 2 to deleting jobs \n"
                               "Enter 3 to view workers details \n"
                               "Enter 4 to add workers\n"
                               "Enter 5 to delete workers\n"
                               "Enter 0 to exit "))
            if choose == 1 :
                adding_jobs()
            elif choose == 3:
                viewing_workers()
            elif choose == 2:
                deleting_jobs()
            elif choose == 0:
                break
            elif choose == 4:
                adding_worker()
            elif choose == 5:
                deleting_workers()
            else:
                print("please enter a number")
        except ValueError:
            print("please enter a number")

menu()
