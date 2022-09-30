import EmployeeClass as e
import PayrollDeductionClass as p

Employee= e.employee('Jimmy Smith',58475,'Information Systems', 'Developer',6800)

fcdeduction= p.PayrollDeduction('food court', '8/14/2022',22.50,39119)
gcdeduction= p.PayrollDeduction('gift contribution','8/12/2022',25.00,58475)
fc2deduction= p.PayrollDeduction('food court', '8/17/2022',15.25,21547)
vmdeduction= p.PayrollDeduction('vending machine','8/22/2022',3.00, 58475)
vm2deduction=p.PayrollDeduction('vending machine', '8/5/2022', 2.75, 58475)

print('*** Employee Pay ***')
print('Name:', e.employee.getname(Employee))
print('ID Number', e.employee.getID(Employee))
print('Department:', e.employee.getdepartment(Employee))
print('Gross Pay: $', float(e.employee.getsal(Employee)), sep='')

netpay=Employee.getsal()

Deductions=[fcdeduction,gcdeduction,fc2deduction,vmdeduction,vm2deduction]
for record in Deductions:
    if p.PayrollDeduction.getID(record)==Employee.getID():
        
        netpay-=p.PayrollDeduction.getamount(record)

print('Net Pay: $',netpay,sep='')


