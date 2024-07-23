from flask import Flask, render_template, request
import math

app = Flask(__name__)

chapters = [
    {"id": 1, "title": "Chapter 1: Understanding Personal Finance", "summary": """Managing and understanding your finances can be difficult, especially if you aren’t a Math or Stats major. Regardless of your understanding of math, you should always evaluate your financial condition relative to your education and career choice. Define your financial goals. Develop a plan of action to achieve your goals. Review your financial progress and make changes as appropriate. Just try to follow these 5 steps and you can help reduce your financial stress and more on what matters most in your life.

If you feel your finances are not good, you should always use these two saving tips which are opportunity costs and trade-offs. Opportunity costs is where you buy the things you need but much cheaper. For example, store brands are usually cheaper than other brand names. Another way is trade-offs. This is a good tool because you focus more on your needs than your wants.
 """},
    {"id": 2, "title": "Chapter 2: Career Planning", "summary": """While taking so many classes at college, you can find many different types of interests; from being a Teacher to being a Doctor. But finding a career is both stressful and may be difficult for some to choose.

	Not only should you learn basic skills such as communication with others but you should also focus on the trends in employment. For example, the news is saying tech and A. I (artificial intelligence) are on the rise and need a lot of people, meaning you should find a career in the tech industry. Or maybe the news are saying that the unemployment rate for Doctors is on the rise which means you should avoid a job in the medical industry.

	But most importantly, regardless of what career you want, you should most definitely find internships or job shadowing opportunities that not only help check of the experiences for job applications but also earn a bit of money before you start your career/job. Although some positions may not pay or pay little, having a lot of experience will help you earn that good pay in your future career. You could start with a pay of $100,000 or higher.
"""},
    {"id": 3, "title": "Chapter 3: Financial Budgets and Tools", "summary": """Do you have a budget?

	Your future depends on planning and budgeting your money. Everybody knows you should spend less than you make, but controlling your spending can be a daunting challenge in the face of so much information and the high cost of living. Here are some concrete actions you can take to help you systematically achieve your financial goals. 

What is the very first thing to do?

	Determine your net income from all sources including part time jobs, scholarships and grants, loans, and so forth.
	
	Identify your expenses. Take into account all monthly expenses and divide them into fixed and variable costs, that is, costs that are consistent versus costs that change from month to month. This includes rent, internet, or loan payments, and food, entertainment and fuel costs respectively. Then you should be equipped to analyze your expenses and reallocate as necessary. 

What kind of tools can you use to keep track of your money?

	Personal finance boils down to bookkeeping and simple planning, that is a record of where your money is coming and going. You can create a simple spreadsheet to help you get started. Getting good visual feedback can help you cut back or replace low-priority purchases. Keeping a detailed log of your money for just one or two months is a good start. 

Use your values to allocate money

	It is important to be self-reflective and think deeply about what you want out of life as this will help guide what purchases you make. Write out what your goals and values are. Graduate with your degree. Pay off your loans. Build credit. 

	Essentials always come first then you can think about things you want. As your goals change you may reevaluate what you deem to be essential. Plans frequently change!
	
Do you have a plan for saving money?

	You don’t need to be told how important saving your money is. Bad things are inevitable, so you should try to be prepared when things go wrong to the best of your ability. As students we may not have the ability to save much money for the time being, but be cognizant of this principle when you get a job, or promotion. Most Americans don’t budget and don’t have an emergency fund, not for any moral failing. Prioritizing essentials might not leave you much left to save so do your best to set aside money each month. 100 dollars a month might be a good place to start. Many people try to save 10-20% of their income. 

Be sure to think of this problem from different timespans. That is to say, try to have a short term and long term plan. Thinking in terms of months and entire semesters and beyond is a good place to start. 

	
Other advice that might be useful if you’ve never heard it before: 
	Take money out of your paycheck before anything else
	Pay credit card balances in full each month
"""},
    {"id": 4, "title": "Chapter 4: Demystifying Taxes", "summary": """Taxes can be intimidating, but rest assured there is nothing you can’t handle. At this stage in your career you probably don’t need to absolutely minimize your tax rate, but just know that there are a variety of ways that you can legally reduce your required contributions. Here it is essential to have a careful record of your expenses. 

	You are required to file taxes to the federal government and the state. How much to each is a complicated question, but certain factors play an important role like your dependency status. There are also ways to reduce what you owe with tax credits. There are also strategies to reduce your tax liability through your employer by participating in certain benefit plans like retirement or healthcare. 


We have a progressive income tax, which means it increases as you earn more money. You don’t pay the same rate on all of your income. The marginal tax rate is the rate at which your last dollar is earned. Think of this like paying different amounts on each chunk of money. Your first chunk of money is taxed at 0%, then the next chunk will be 10%, the next at 15% all the way up. Another rate to keep in mind is the effective marginal tax rate, which tells you the total tax you pay on your income. 

	There is a multi-step process starting with your total income and subtracting certain amounts to determine how much money you owe, but suffice to say, you can probably use software or a calculator to determine this. It is worth noting the IRS has a tool you can use for free called the IRS Free File if your adjusted gross income is under 79,000 a year. 

	Individual tax laws change and your situation will vary, so talk to a professional if necessary! 
"""},
    {"id": 5, "title": "Chapter 5: Managing Checking and Savings Accounts", "summary": """Managing your money wisely is crucial, especially as a college freshman. The main goal of managing your monetary assets is to maximize the interest you earn on savings and minimize fees on your accounts. Banks and credit unions are your primary sources for these services, offering insured accounts to keep your money safe. For everyday expenses, put cash into a checking account, and consider opening a money market account for future investments. Many banks offer student checking accounts with lower balance requirements. Savings accounts usually offer higher interest rates than checking accounts, and certificates of deposit (CDs) can provide fixed interest rates over time.

When setting up accounts, think about ownership: individual accounts can have a "payable on death" arrangement to transfer ownership directly to a beneficiary, while joint accounts, often used by married couples, come with a "right of survivorship."

Electronic banking is convenient and includes tools like ATMs, debit cards, and online banking. It's protected by the Electronic Funds Transfer Act, which also includes error resolution processes.

Lastly, discussing finances with your loved ones is important. Understand your own money habits and communicate openly using "I" statements to navigate any financial issues, especially in complex family situations. """},
    {"id": 6, "title": "Chapter 6: Building and Maintaining Good Credit", "summary": """Using credit has both advantages and disadvantages. Credit can help you manage financial emergencies, get goods immediately, and secure future discounts. However, the main downside is the potential loss of financial flexibility. To protect against identity theft, consider using a credit freeze.

Setting a debt limit is crucial and can be done using three methods: the continuous-debt method, the debt-to-income method, and the debt payments-to-disposable income method. It's also important to keep your student loan debt under control.

To build and maintain good credit, start with a credit application and understand your credit report. Lenders use this to decide on your application and set interest rates. Improving your credit history will boost your credit score, with FICO scores being particularly significant. If there are errors on your credit report, you can have them corrected.

Watch for signs of overindebtedness, such as exceeding credit limits and frequently running out of money. If you face serious financial difficulties, seek help from nonprofit credit counseling agencies or consult an attorney about bankruptcy options."""},
    {"id": 7, "title": "Chapter 8: Vehicle and Other Major Purchases", "summary": """The first steps in smart buying involve prioritizing your wants, gathering information through research, and making sure the planned purchase fits your budget. These steps help you prepare before interacting with sellers.

When it’s time to shop, comparison shopping is key to finding the best deal, especially for big-ticket items like cars. This means looking at safety features, financing options, interest rates, leasing terms, warranties, and service contracts.

Successful negotiation is essential when making major purchases. This involves haggling for a fair price, understanding dealer incentives, negotiating the price, interest rates, and trade-ins, using a decision-making matrix, finalizing the deal, and evaluating your decision afterward.

If something goes wrong with your purchase, there are effective complaint procedures you can use, such as the FTC’s cooling-off rule, mediation, arbitration, lemon laws, or small-claims court. These can help resolve issues and ensure you're treated fairly."""},
    {"id": 8, "title": "Chapter 9: Affordable Housing", "summary": """Right now there is a housing shortage just about everywhere in the country, but it is especially difficult to find here in Monterey. So as college students we are fighting an uphill battle to simply have a roof over our heads. Around 10% of our fellow classmates are homeless as a consequence of this. 

Do you know how to obtain affordable housing?             

	When you graduate you will need to make a decision on if you rent or buy a home, but for most students it is simply easier to rent as it is temporary and less expensive so you can focus on your education. 

	You can explore off campus options for rent if the school cannot provide an affordable option. There are social media groups like NEW HOMELESS OTTERS OF CSUMB/Monterey on Facebook that are specifically for posting about housing inquiries. Other sites like Craigslist, Nextdoor, or even Myraft may be good places to seek out new homes and roommates. 

	In a high cost of living area it’s likely you will need one or more roommates to split the costs with. This may afford you more space and cheaper rent in the long run. Keep in mind that as a tenant you have rights to live in dignity and security. 
	
You have a right to equal opportunity housing, a refundable security deposit, the right to information about mold utilities and so on, a habitable place to live, privacy, protection from wrongful eviction, and rent control. You also have a right against retaliatory actions like being evicted because you requested a repair. A landlord cannot increase rent more than 8.3% in a 12 month period in Monterey county

	Once you graduate, it will be good to think about home ownership because it is far cheaper in the long run by owning a home. At the end of the day, you’re going to buy somebody a new house, how you manage your money will determine if that house belongs to you or some absentee landlord. So in this time focus on building your credit and saving what you can in order to set yourself up for being able to buy property later down the road. 
"""},
    {"id": 9, "title": "Chapter 13: Investment Fundamentals", "summary": """ You have all the brains, the experience, and of course the money. But now you have all these bills to pay. Sometimes you are left with a small amount of money and probably store it in your savings account which may accuracy low interest rates on it. Even if you have some leftover money, you can not only put it in your savings account, but you can grow your income to new heights.

	You can use your leftover money to invest in it through dividends. Dividends is where you buy a share of a company and act as a boss. If you buy a share of 5%, you control 5% of the company. As a token of it, your value of it will grow which means you can earn money off from it.

	Slam dunk but you need to pay taxes on it since it’s a source of income. You would have to pay a high marginal tax rate between 20-25% depending on local, state, and federal tax laws. But if you make capital gains, you would pay roughly half on it depending on tax laws in the U.S. When your value of share goes up at the time you sell it, you get a capital gain. But if it goes down, you of course experience a capital loss.

	However you invest, use it to pay off student loans and focus more on your wants. But remember to pay your taxes on these or the I.R.S would find you and either have your arrested or pay a big fine bigger than the amount of taxes you pay on a yearly basis.
"""},

]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/chapters')
def chapters_list():
    return render_template('chapters.html', chapters=chapters)

@app.route('/chapter/<int:chapter_id>')
def chapter(chapter_id):
    chapter = next((c for c in chapters if c['id'] == chapter_id), None)
    if chapter:
        return render_template('chapter.html', chapter=chapter)
    return "Chapter not found", 404

@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        monthly_investment = float(request.form['monthly_investment'])
        years = int(request.form['years'])
        annual_return = 0.07  # Assumed 7% annual return
        months = years * 12
        total = monthly_investment * ((1 + annual_return/12) ** months - 1) / (annual_return/12)
        total = round(total, 2)
        result = f"If you invest ${monthly_investment} monthly for {years} years, you could have ${total:,} in your IRA."
    return render_template('calculator.html', result=result)

@app.route('/budget', methods=['GET', 'POST'])
def budget():
    if request.method == 'POST':
        income = float(request.form['income'])
        expenses = {
            'rent': float(request.form['rent']),
            'food': float(request.form['food']),
            'utilities': float(request.form['utilities']),
            'transportation': float(request.form['transportation']),
            'entertainment': float(request.form['entertainment']),
            'other': float(request.form['other'])
        }
        total_expenses = sum(expenses.values())
        balance = income - total_expenses
        
        return render_template('budget_result.html', income=income, expenses=expenses, total_expenses=total_expenses, balance=balance)
    
    return render_template('budget_form.html')

if __name__ == '__main__':
    app.run(debug=True)