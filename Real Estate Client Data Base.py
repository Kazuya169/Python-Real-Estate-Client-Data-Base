from tkinter import*
from tkinter import ttk
import random
import time
import datetime
import tkinter.messagebox

class Client:

    def __init__(self,root):
        self.root = root
        self.root.title("Real Estate Client Data Base")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background='white')


        cmbFullName=StringVar()
        ContactInformation=StringVar()
        DateofBirth=StringVar()
        MaritalStatus=StringVar()
        Occupation=StringVar()
        Income=StringVar()
        PreferredfortheProperty=StringVar()
        TypeofProperty=StringVar()
        BudgetFinancingDetails=StringVar()
        TimelineforthePropertySearchandPurchase=StringVar()
        PreferredMoveinDate=StringVar()
        SpecificNeedsorSpecialRequirments=StringVar()
        DesiredFeaturesorMustHaveItems=StringVar()
        AnnualIncomeandSourcesofIncome=StringVar()
        ExistingAssets=StringVar()
        PreferredLoanType=StringVar()
        PastRealEstateExpirience=StringVar()
        PreferredCommunicationMethodsFrequency=StringVar()
        Description=StringVar()
        #############Function Mdeclaration##########
        def iExit():
            iExit=tkinter.messagebox.askyesno("Real Estate Client Data Base","Confirm if you want to exit")
            if iExit >0:
                root.destroy()
                return
        
        def iDescription():
            
            self.txtDescription.insert(END,'Full Name: \t\t'+ cmbFullName.get() + "\n")
            self.txtDescription.insert(END,'ContactInformation: \t\t'+ ContactInformation.get() + "\n")
            self.txtDescription.insert(END,'DateofBirth: \t\t'+ DateofBirth.get() + "\n")
            self.txtDescription.insert(END,'MaritalStatus: \t\t'+ MaritalStatus.get() + "\n")
            self.txtDescription.insert(END,'Occupation: \t\t'+ Occupation.get() + "\n")
            self.txtDescription.insert(END,'Income: \t\t'+ Income.get() + "\n")
            self.txtDescription.insert(END,'PreferredfortheProperty: \t\t'+ PreferredfortheProperty.get() + "\n")
            self.txtDescription.insert(END,'TypeofProperty: \t\t'+ TypeofProperty.get() + "\n")
            self.txtDescription.insert(END,'BudgetFinancingDetails: \t\t'+ BudgetFinancingDetails.get() + "\n")
            self.txtDescription.insert(END,'TimelineforthePropertySearchandPurchase: \t\t'+ TimelineforthePropertySearchandPurchase.get() + "\n")
            self.txtDescription.insert(END,'PreferredMoveinDate: \t\t'+ PreferredMoveinDate.get() + "\n")
            self.txtDescription.insert(END,'SpecificNeedsorSpecialRequirments: \t\t'+ SpecificNeedsorSpecialRequirments.get() + "\n")
            self.txtDescription.insert(END,'DesiredFeaturesorMustHaveItems: \t\t'+ DesiredFeaturesorMustHaveItems.get() + "\n")
            self.txtDescription.insert(END,'AnnualIncomeandSourcesofIncome: \t\t'+ AnnualIncomeandSourcesofIncome.get() + "\n")
            self.txtDescription.insert(END,'ExistingAssets: \t\t'+ ExistingAssets.get() + "\n")
            self.txtDescription.insert(END,'PreferredLoanType: \t\t'+ PreferredLoanType.get() + "\n")
            self.txtDescription.insert(END,'PastRealEstateExpirience: \t\t'+ PastRealEstateExpirience.get() + "\n")
            self.txtDescription.insert(END,'PreferredCommunicationMethodsFrequency: \t\t'+ PreferredCommunicationMethodsFrequency.get() + "\n")
            return
        
        def iDescriptionData():
            ############################### DIPA TAPOS TOHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH################3

            self.txtFrameDetail.insert(END, cmbFullName.get()+"\t"+ContactInformation.get()+"\t"+DateofBirth.get()+"\t""\t"+MaritalStatus.get()+ "\t""\t"+Occupation.get()+"\t""\t"+Income.get()+ "\t""\t"+PreferredfortheProperty.get()+
            "\t""\t""\t"+TypeofProperty.get()+ "\t""\t"+BudgetFinancingDetails.get()+ "\t""\t""\t""\t"+PreferredMoveinDate.get()+ "\t""\t""\t"+DesiredFeaturesorMustHaveItems.get() +"\t""\t"+PreferredLoanType.get() + "\n")
            
            return
        
        def iDelete():

            cmbFullName.set("")
            ContactInformation.set("")
            DateofBirth.set("")
            MaritalStatus.set("")
            Occupation.set("")
            Income.set("")
            PreferredfortheProperty.set("")
            TypeofProperty.set("")
            BudgetFinancingDetails.set("")
            TimelineforthePropertySearchandPurchase.set("")
            PreferredMoveinDate.set("")
            SpecificNeedsorSpecialRequirments.set("")
            DesiredFeaturesorMustHaveItems.set("")
            AnnualIncomeandSourcesofIncome.set("")
            ExistingAssets.set("")
            PreferredLoanType.set("")
            PastRealEstateExpirience.set("")
            PreferredCommunicationMethodsFrequency.set("")
            self.txtDescription.delete("1.0",END)
            self.txtFrameDetail.delete("1.0",END)

            return
        
        def iReset():
            cmbFullName.set("")
            ContactInformation.set("")
            DateofBirth.set("")
            MaritalStatus.set("")
            Occupation.set("")
            Income.set("")
            PreferredfortheProperty.set("")
            TypeofProperty.set("")
            BudgetFinancingDetails.set("")
            TimelineforthePropertySearchandPurchase.set("")
            PreferredMoveinDate.set("")
            SpecificNeedsorSpecialRequirments.set("")
            DesiredFeaturesorMustHaveItems.set("")
            AnnualIncomeandSourcesofIncome.set("")
            ExistingAssets.set("")
            PreferredLoanType.set("")
            PastRealEstateExpirience.set("")
            PreferredCommunicationMethodsFrequency.set("")
            self.txtDescription.delete("1.0",END)
            self.txtFrameDetail.delete("1.0",END)

            return
       


        #############FRAME#################
        MainFrame =Frame(self.root)
        MainFrame.grid()

        TitleFrame = Frame(MainFrame,bd=20, width=1350, padx=20, relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle =Label(TitleFrame, width=39, font=('arial', 40, 'bold'), text="Real Estate Client Data Base",padx=100,pady=10)
        self.lblTitle.grid()

        FrameDetail =Frame(MainFrame,bd=20, width=1350, height=100, padx=10,pady=4, relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        ButtonFrame =Frame(MainFrame,bd=20, width=1350, height=50, padx=30,pady=4, relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame =Frame(MainFrame,bd=20, width=1350, height=400, padx=30,pady=4, relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT =LabelFrame(DataFrame,bd=10, width=800, height=300, padx=2,pady=4, relief=RIDGE,
                             font=('arial', 12, 'bold'), text="Client Information:",)
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT =LabelFrame(DataFrame,bd=10, width=450, height=300, padx=10,pady=10, relief=RIDGE,
                                   font=('arial', 12, 'bold'), text="Description:",)
        DataFrameRIGHT.pack(side=RIGHT)
                               ###################DATA FRAME LEFT NEH################
        self.lblFullName =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Full Name",padx=2, pady=4)
        self.lblFullName.grid(row=0, column=0,sticky=W)

        self.txtFullName=Entry(DataFrameLEFT, font=('arial', 12, 'bold'),textvariable =cmbFullName)
        self.txtFullName.grid(row=0, column=1)
                       
        self.lblTimelineforthePropertySearchandPurchase =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Timeline for the Property Search and Purchase:",padx=2,pady=4)
        self.lblTimelineforthePropertySearchandPurchase.grid(row=0, column=2,sticky=W)
        self.txtTimelineforthePropertySearchandPurchase=Entry(DataFrameLEFT, font=('arial', 12, 'bold'),textvariable =TimelineforthePropertySearchandPurchase)
        self.txtTimelineforthePropertySearchandPurchase.grid(row=0, column=3)

        self.lblContactInformation =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Contact Information:",padx=2,pady=4)
        self.lblContactInformation.grid(row=1, column=0,sticky=W)
        self.txtContactInformation=Entry(DataFrameLEFT, font=('arial', 12, 'bold'),textvariable =ContactInformation)
        self.txtContactInformation.grid(row=1, column=1)

        self.lblPreferredMoveinDate=Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="     Preferred Move in Date:",padx=2,pady=4)
        self.lblPreferredMoveinDate.grid(row=1, column=2,)
        self.txtPreferredMoveinDate=Entry(DataFrameLEFT, font=('arial', 12, 'bold'),textvariable =PreferredMoveinDate)
        self.txtPreferredMoveinDate.grid(row=1, column=3)

        self.lblDateofBirth =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Date of Birth:",padx=2,pady=4)
        self.lblDateofBirth.grid(row=2, column=0,sticky=W)
        self.txtDateofBirth=Entry(DataFrameLEFT, font=('arial', 12, 'bold'),textvariable =DateofBirth)
        self.txtDateofBirth.grid(row=2, column=1)

        self.lblSpecificNeedsorSpecialRequirments=Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Specific Needs or Special Requirments:",padx=2,pady=4)
        self.lblSpecificNeedsorSpecialRequirments.grid(row=2, column=2,)
        self.txtSpecificNeedsorSpecialRequirments=Entry(DataFrameLEFT, font=('arial', 12, 'bold'),textvariable =SpecificNeedsorSpecialRequirments)
        self.txtSpecificNeedsorSpecialRequirments.grid(row=2, column=3)

        self.lblMaritalStatus =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Marital Status:",padx=2,pady=4)
        self.lblMaritalStatus.grid(row=3, column=0,sticky=W)
        self.txtMaritalStatus=Entry(DataFrameLEFT, font=('arial', 12, 'bold'),textvariable =MaritalStatus)
        self.txtMaritalStatus.grid(row=3, column=1)

        self.lblDesiredFeaturesorMustHaveItems=Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Desired Features or Must Have Items:",padx=2,pady=4)
        self.lblDesiredFeaturesorMustHaveItems.grid(row=3, column=2,)
        self.txtDesiredFeaturesorMustHaveItems=Entry(DataFrameLEFT, font=('arial', 12, 'bold'),textvariable =DesiredFeaturesorMustHaveItems)
        self.txtDesiredFeaturesorMustHaveItems.grid(row=3, column=3)

        self.lblOccupation =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Occupation:",padx=2,pady=4)
        self.lblOccupation.grid(row=4, column=0,sticky=W)
        self.txtOccupation=Entry(DataFrameLEFT, font=('arial', 12, 'bold'),textvariable =Occupation)
        self.txtOccupation.grid(row=4, column=1)

        self.lblAnnualIncomeandSourcesofIncome=Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Annual Income and Sources of Income:",padx=2,pady=4)
        self.lblAnnualIncomeandSourcesofIncome.grid(row=4, column=2,)
        self.txtAnnualIncomeandSourcesofIncome=Entry(DataFrameLEFT, font=('arial', 12, 'bold'),textvariable =AnnualIncomeandSourcesofIncome)
        self.txtAnnualIncomeandSourcesofIncome.grid(row=4, column=3)

        self.lblIncome =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Income:",padx=2,pady=4)
        self.lblIncome.grid(row=5, column=0,sticky=W)
        self.txtIncome=Entry(DataFrameLEFT, font=('arial', 12, 'bold'),textvariable =Income)
        self.txtIncome.grid(row=5, column=1)

        self.lblExistingAssets=Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Existing Assets:",padx=2,pady=4)
        self.lblExistingAssets.grid(row=5, column=2,)
        self.txtExistingAssets=Entry(DataFrameLEFT, font=('arial', 12, 'bold'),textvariable =ExistingAssets)
        self.txtExistingAssets.grid(row=5, column=3)

        self.lblPreferredfortheProperty =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Preferred for the Property:",padx=2,pady=4)
        self.lblPreferredfortheProperty.grid(row=6, column=0,sticky=W)
        self.txtPreferredfortheProperty=Entry(DataFrameLEFT, font=('arial', 12, 'bold'),textvariable =PreferredfortheProperty)
        self.txtPreferredfortheProperty.grid(row=6, column=1)

        self.lblPreferredLoanType=Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Preferred Loan Type:",padx=2,pady=4)
        self.lblPreferredLoanType.grid(row=6, column=2,)
        self.txtPreferredLoanType=Entry(DataFrameLEFT, font=('arial', 12, 'bold'),textvariable =PreferredLoanType)
        self.txtPreferredLoanType.grid(row=6, column=3)

        self.lblTypeofProperty =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Type of Property:",padx=2,pady=4)
        self.lblTypeofProperty.grid(row=7, column=0,sticky=W)
        self.txtTypeofProperty=Entry(DataFrameLEFT, font=('arial', 12, 'bold'),textvariable =TypeofProperty)
        self.txtTypeofProperty.grid(row=7, column=1)
        
        self.lblPastRealEstateExpirience=Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Past Real Estate Expirience:",padx=2,pady=4)
        self.lblPastRealEstateExpirience.grid(row=7, column=2,)
        self.txtPastRealEstateExpirience=Entry(DataFrameLEFT, font=('arial', 12, 'bold'),textvariable =PastRealEstateExpirience)
        self.txtPastRealEstateExpirience.grid(row=7, column=3)

        self.lblBudgetFinancingDetails =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Budget Financing Details:",padx=2,pady=4)
        self.lblBudgetFinancingDetails.grid(row=8, column=0,sticky=W)
        self.txtBudgetFinancingDetails=Entry(DataFrameLEFT, font=('arial', 12, 'bold'),textvariable =BudgetFinancingDetails)
        self.txtBudgetFinancingDetails.grid(row=8, column=1)

        self.lblPreferredCommunicationMethodsFrequency=Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Preferred Communication Methods Frequency:",padx=2)
        self.lblPreferredCommunicationMethodsFrequency.grid(row=8, column=2,)
        self.txtPreferredCommunicationMethodsFrequency=Entry(DataFrameLEFT, font=('arial', 12, 'bold'),textvariable =PreferredCommunicationMethodsFrequency)
        self.txtPreferredCommunicationMethodsFrequency.grid(row=8, column=3)

                                                     ###################DATA FRAME RIGHT NEH################
        self.txtDescription= Text(DataFrameRIGHT, font=('arial', 12, 'bold'), width=45, height=12, padx=2,pady=24)
        self.txtDescription.grid(row=0, column=0,)

                                                     ###################Button Frame NEH################
        self.btnDescription=Button(ButtonFrame,text='Description',font=('arial', 12, 'bold'), width=27,bd=5,
                                   command=iDescription)
        self.btnDescription.grid(row=0,column=0)
        self.btnDescriptionData=Button(ButtonFrame,text='Description Data',font=('arial', 12, 'bold'), width=27,bd=5,
                                   command=iDescriptionData)
        self.btnDescriptionData.grid(row=0,column=1)
        self.btnDelete=Button(ButtonFrame,text='Delete',font=('arial', 12, 'bold'), width=27,bd=5,
                              command=iDelete)
        self.btnDelete.grid(row=0,column=2)
        self.btnReset=Button(ButtonFrame,text='Reset',font=('arial', 12, 'bold'), width=27,bd=5,
                             command=iReset)
        self.btnReset.grid(row=0,column=3)
        self.btnExit=Button(ButtonFrame,text='Exit',font=('arial', 12, 'bold'), width=27,bd=5,
                            command=iExit)
        self.btnExit.grid(row=0,column=4)





                                                     ###################Frame Detail NEH################
        self.lblLabel = Label(FrameDetail, font=('arial',10,'bold'),pady=4,
        text="Clients\tContact\tDate of Birth\tMarital Status\tOccupation\tIncome\t\tPreferred Property\tType of Property\t Budget Financing Details\t\tPreferred Move in Date\tDesired Features\tPreferred Loan Type",)
        self.lblLabel.grid(row=0, column=0,)


        self.txtFrameDetail= Text(FrameDetail, font=('arial',10, 'bold'), width=210, height=7, padx=2,pady=4)
        self.txtFrameDetail.grid(row=1, column=0,)




if __name__=='__main__':
    root = Tk()
    application = Client(root)
    root.mainloop()










