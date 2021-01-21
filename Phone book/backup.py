from tkinter import *
from tkinter import messagebox as tmsg
from contact import *
from itertools import cycle
from PIL import Image,ImageTk
from time import sleep

class GUI(Tk):

    def __init__(self):
        super().__init__()
        self.iconbitmap("contacts.ico")
        self.geometry("500x550")
        self.resizable(False,False)
        
        self.title("Phone Book v1.0.1")

        self.colors = cycle(["#FFBD05","#FFD766"])
        self.frame = Frame(self)

    
        self.image = Image.open("contacts.jpg")
        
        self.image = ImageTk.PhotoImage(self.image)
        self.label = Label(self.frame,image = self.image)
        self.label.place(relx = 0,rely = 0,relwidth = 1,relheight = 1)
        self.frame.place(relx = 1/5,rely = 1/5,relwidth = 3/5,relheight = 3/5)
        
        for i in range(3):
            self.label.update()
            self.frame.update()
            sleep(1)
        self.frame.update()
    def first_view(self):
        self.frame = Frame(self,bg = "#FF9585")
        self.frame.update()
        self.frame.place(relx = 0,rely = 0,relwidth = 1,relheight = 1)

        self.header = Label(self.frame,text = "My Phone Book",font = "comicsansms 25 bold",padx = 5,
        fg = "#008A7A",bg = "#FF9585")
        self.header.place(relx = 0 ,rely = 0,relwidth = 1,relheight = 0.2)

        self.quote = Label(self.frame,text = "-Perfect stop to manage your business contacts",font = "comicsansms 15",
        fg = "#008A7A",bg = "#FF9585")
        self.quote.place(relx = 0,rely = 0.2,relheight = 8/85,relwidth = 1)

        self.add_button = Button(self.frame,text = "Add New Contact",font = "comicsansms 15",bg = "#006885",fg = "#E0FF4C",
        activeforeground = "lime",activebackground = "black",command = self.add_contact_win)
        self.add_button.place(relx = 1/5,rely = 0.2+16/85,relheight = 8/85,relwidth = 3/5)

        self.show_button = Button(self.frame,text = "Show And Edit My Contacts ",font = "comicsansms 15",bg = "#006885",fg = "#E0FF4C",
        activeforeground = "lime",activebackground = "black",command = self.display_all_contacts)
        self.show_button.place(relx = 1/5,rely = 0.2+16/85 + 12/85,relheight = 8/85,relwidth = 3/5)

        self.delete_button = Button(self.frame,text = "Delete a Contact",font = "comicsansms 15",bg = "#006885",fg = "#E0FF4C",
        activeforeground = "lime",activebackground = "black",command = self.delete_contact_win)
        self.delete_button.place(relx = 1/5,rely = 0.2+16/85 + 24/85,relheight = 8/85,relwidth = 3/5)

        self.about_button = Button(self.frame,text = "About Us",font = "comicsansms 15",bg = "#006885",fg = "#E0FF4C",
        activeforeground = "lime",activebackground = "black",command = self.about_us)
        self.about_button.place(relx = 1/5,rely =0.2+16/85 + 36/85,relheight = 8/85,relwidth = 3/5)

        self.exit_button = Button(self.frame,text = "EXIT",font = "comicsansms 15",bg = "#7434EA",fg = "lime",command = self.destroy,
        activebackground = "#7434EA")
        self.exit_button.place(relx = 4/5,relwidth = 1/5,relheight = 8/85,rely = 0.2+16/85 + 36/85 + 8/85)
    def delete_contact_win(self):
        
        self.show_list_contacts("delete")
        
        for record in self.records:
            self.current = Button(self.dummy_frame,text = f"{record[0]:<15}{record[1]:<15}",anchor = "w",
            font = "comicsansms 15",padx = 100,pady = 10,bg = next(self.colors),fg = "#DC2C28")
            self.current.pack(fill = X,anchor = "w")
            self.current.bind("<Button-1>",self.delete_me)
        tmsg.showinfo("Pro Tip","Click desired contact to delete it!")
        
    def delete_me(self,event):        
        self.name = " ".join(event.widget.cget("text").split()[:-1])
        self.record = Contact.contact_lookup(self.name)

        #message ask
        ans = tmsg.askyesno("Confirm delete","Are you sure ,you want to delete this contact?")
        temp_rec = Contact(*self.record)

        if ans:
            temp_rec.remove_contact_from_database()
            message = "Contact removed successfully"
            tmsg.showinfo("Deletion Done",message)
        self.delete_contact_win()

    def add_contact_win(self):
        self.frame.place_forget()
        self.frame = Frame(self,bg = "#FF9585")

        self.detail_header = Label(self.frame,bg = "#FF9585",fg = "#008A7A",text = "Details",font = "comicsansms 17 bold")
        self.detail_header.place(relx = 0,rely = 0,relwidth = 1,relheight = 3/41)

        self.name_label = Label(self.frame,bg = "#FF9585",fg = "#008A7A",font = "comicsansms 15 ",text = "Name")
        self.name_label.place(relx = 1/14,rely = 4/41,relwidth = 3/7,relheight = 3/41)
        self.name_entry = Entry(self.frame,font = "comicsansms 15",bg = "#FF7AF8")
        self.name_entry.place(relx = 0.5,rely = 4/41 ,relwidth = 3/7,relheight = 3/41)

        self.nationality_label = Label(self.frame,bg = "#FF9585",fg = "#008A7A",font = "comicsansms 15 ",text = "Nationality")
        self.nationality_label.place(relx = 1/14,rely = 8/41,relwidth = 3/7,relheight = 3/41)
        self.nationality_entry = Entry(self.frame,font = "comicsansms 15",bg = "#FF7AF8")
        self.nationality_entry.place(relx = 0.5,rely = 8/41,relwidth = 3/7,relheight = 3/41)

        self.phone_label = Label(self.frame,bg = "#FF9585",fg = "#008A7A",font = "comicsansms 15 ",text = "Phone")
        self.phone_label.place(relx = 1/14,rely = 12/41,relwidth = 3/7,relheight = 3/41)
        self.phone_entry = Entry(self.frame,font = "comicsansms 15",bg = "#FF7AF8")
        self.phone_entry.place(relx = 0.5,rely = 12/41,relwidth = 3/7,relheight = 3/41)

        self.note_label = Label(self.frame,bg = "#FF9585",fg = "#008A7A",font = "comicsansms 15",text = "Note",anchor = "w")
        self.note_label.place(anchor = "w",relx = 1/14,rely = 16/41,relheight = 3/82,relwidth = 3/7)
        self.note_text = Text(self.frame,wrap = WORD,font = "comicsansms 10",padx = 5,pady = 5,height = 10,width = 60,bg = "#FF7AF8")
        self.note_text.place(relx = 1/14,rely = 35/82,relheight = 15/82,relwidth = 6/7)

        self.profession_label = Label(self.frame,bg = "#FF9585",fg = "#008A7A",font = "comicsansms 15",text = "Profession")
        self.profession_label.place(relx = 1/14,relheight = 3/41,relwidth = 3/7,rely = 29/41)
        self.profession_entry = Entry(self.frame,font = "comicsansms 15",bg = "#FF7AF8")
        self.profession_entry.place(relx = 0.5,relheight = 3/41,relwidth = 3/7,rely = 29/41)

        self.address_label = Label(self.frame,bg = "#FF9585",fg = "#008A7A",font = "comicsansms 15",text = "Address")
        self.address_label.place(relx = 1/14,relheight = 3/41,relwidth = 3/7,rely = 33/41)
        self.address_entry = Entry(self.frame,font = "comicsansms 15",bg = "#FF7AF8")
        self.address_entry.place(relx = 0.5,relheight = 3/41,relwidth = 3/7,rely = 33/41)

        self.back_button = Button(self.frame,text = "Back",font  = "comicsansms 15",bg = "#7434EA",fg = "lime",
        command = self.first_view,borderwidth = 3,activebackground = "#7434EA")
        self.back_button.place(relx = 1/10,rely = 37/41,relwidth = 1/5,relheight = 3/41)

        self.save_button = Button(self.frame,text = "Save",font  = "comicsansms 15",bg = "#7434EA",fg = "lime",
        borderwidth = 3,command = self.save_info,activebackground = "#7434EA")
        self.save_button.place(relx = 7/10,rely = 37/41,relwidth = 1/5,relheight = 3/41)

        self.frame.place(relx = 0,rely = 0,relheight = 1,relwidth = 1)

    def save_info(self):
        """To extract from entries and push into Database """
        name = self.name_entry.get()
        nationality = self.nationality_entry.get()
        phone = self.phone_entry.get()
        note = self.note_text.get(1.0,END)
        profession = self.profession_entry.get()
        address = self.address_entry.get()

        if name.isspace() or not name:
            tmsg.showerror("OHOH","Name is required!")
        
        elif phone.isspace() or not phone:
            phone = "0"
            my_contact = Contact(name,nationality,int(phone),note,profession,address)
            my_contact.delete_if_exists_then_add()
            tmsg.showinfo("Ok","Contact has been successfully saved")

        elif not phone.isdigit():
            tmsg.showerror("Wait a min","Enter valid phone")
    
        else:
            my_contact = Contact(name,nationality,int(phone),note,profession,address)
            my_contact.delete_if_exists_then_add()
            tmsg.showinfo("Ok","Contact has been successfully saved")


    def display_all_contacts(self):
        self.show_list_contacts()
        
        for record in self.records:
            self.current = Button(self.dummy_frame,text = f"{record[0]:<15}{record[1]:<15}",anchor = "w",
            font = "comicsansms 15",padx = 120,pady = 10,bg = next(self.colors),fg = "#DC2C28")
            self.current.pack(fill = X,anchor = "w")
            self.current.bind("<Button-1>",self.display_contact_info)

    def display_contact_info(self,event):
       self.name = " ".join(event.widget.cget("text").split()[:-1])
       
       self.record = Contact.contact_lookup(self.name)
       
    
       self.add_contact_win()
       self.name_entry.insert(0,self.record[0])
       self.nationality_entry.insert(0,self.record[1])
       self.phone_entry.insert(0,self.record[2])
       self.note_text.insert(1.0,self.record[3])
       self.profession_entry.insert(0,self.record[4])
       self.address_entry.insert(0,self.record[5])
       self.back_button["command"] = self.display_all_contacts

    def show_list_contacts(self,purpose = None):
        self.frame.place_forget()

        
        self.scroll = Scrollbar(self.frame)
                
        self.frame = Frame(self,bg = "#FF9585")
        self.frame.place(relx = 0,rely = 0,relwidth = 1,relheight = 1)
        
        self.search_image = Image.open("search.png")
        self.search_image = ImageTk.PhotoImage(self.search_image)
        if purpose is None:
            self.search_button = Button(self.frame,image = self.search_image,command = self.show_filtered_results)
        else:
            self.search_button = Button(self.frame,image = self.search_image,command = lambda : self.show_filtered_results("delete"))
        self.search_button.place(relx = 1/14,rely = 1/12,relheight = 1/12,relwidth = 1/7)

        self.search_entry = Entry(self.frame,font = "comicsansms 15")
        self.search_entry.place(relx = 3/14,rely = 1/12,relheight = 1/12,relwidth = 3/7)

        self.options = ["NAME","NATIONALITY","NOTE","ALL"]
        self.filter_var = StringVar()
        self.filter_var.set("Search By")

        self.drop_down = OptionMenu(self.frame,self.filter_var,*self.options)
        self.drop_down.place(relx = 9/14,rely = 1/12,relheight = 1/12,relwidth = 2/7)

        self.contact_header = Label(self.frame,bg = "#FF9585",fg = "#008A7A",font = "comicsansms 17 bold",text = "My Contacts")
        self.contact_header.place(relx = 0,rely = 0,relwidth = 1,relheight = 1/12)

        self.contact_frame = Frame(self.frame,bg = "#FF9585")
        self.contact_frame.place(relx = 1/14,rely = 2/12,relheight = 4/6+1/12,relwidth = 6/7)

        self.back_button = Button(self.frame,text = "Back",fg = "lime",bg = "#7434EA",command = self.first_view,font = "comicsansms 15",
        activebackground = "#7434EA")
        self.back_button.place(relx = 5/14,rely = 11/12,relheight = 1/12,relwidth = 2/7)

       
        self.canvas = Canvas(self.contact_frame,bg = "#FF9585")
        self.dummy_frame = Frame(self.canvas,bg = "#FF9585")
        self.my_scrollbar = Scrollbar(self.contact_frame,orient = VERTICAL,command = self.canvas.yview)
        self.canvas.configure(yscrollcommand = self.my_scrollbar.set)

        self.my_scrollbar.pack(side = RIGHT,fill = Y)
        self.canvas.pack(side = LEFT)
        self.canvas.create_window((0,0),window = self.dummy_frame,anchor = "nw")
        self.dummy_frame.bind("<Configure>",lambda e:self.canvas.configure(scrollregion = self.canvas.bbox("all"),width = 410,height = 600))

        #fetching all contacts from DB
        self.records = Contact.get_all_contacts()

    def show_filtered_results(self,purpose = None):
        key = self.filter_var.get()
        value = self.search_entry.get()
        self.records = Contact.contact_lookup_by_field_matching(key,value)

        if self.records is None or self.records == []:
            tmsg.showerror("OOPS","No such results found")
            self.records = Contact.get_all_contacts()
            self.display_all_contacts()
        else:
            self.frame.place_forget()        
            self.scroll = Scrollbar(self.frame)
                
            self.frame = Frame(self,bg = "#FF9585")
            self.frame.place(relx = 0,rely = 0,relwidth = 1,relheight = 1)
        
            self.search_image = Image.open("search.png")
            self.search_image = ImageTk.PhotoImage(self.search_image)
            self.search_button = Button(self.frame,image = self.search_image,command = self.show_filtered_results)
            self.search_button.place(relx = 1/14,rely = 1/12,relheight = 1/12,relwidth = 1/7)

            self.search_entry = Entry(self.frame,font = "comicsansms 15")
            self.search_entry.place(relx = 3/14,rely = 1/12,relheight = 1/12,relwidth = 3/7)

            self.options = ["NAME","NATIONALITY","NOTE","ALL"]
            self.filter_var = StringVar()
            self.filter_var.set("Search By")

            self.drop_down = OptionMenu(self.frame,self.filter_var,*self.options)
            self.drop_down.place(relx = 9/14,rely = 1/12,relheight = 1/12,relwidth = 2/7)

            self.contact_header = Label(self.frame,bg = "#FF9585",fg = "#008A7A",font = "comicsansms 17 bold",text = "My Contacts")
            self.contact_header.place(relx = 0,rely = 0,relwidth = 1,relheight = 1/12)

            self.contact_frame = Frame(self.frame,bg = "#FF9585")
            self.contact_frame.place(relx = 1/14,rely = 2/12,relheight = 4/6+1/12,relwidth = 6/7)

            self.back_button = Button(self.frame,text = "Back",fg = "lime",bg = "#7434EA",command = self.first_view,font = "comicsansms 15",
            activebackground = "#7434EA")
            self.back_button.place(relx = 5/14,rely = 11/12,relheight = 1/12,relwidth = 2/7)

       
            self.canvas = Canvas(self.contact_frame,bg = "#FF9585")
            self.dummy_frame = Frame(self.canvas,bg = "#FF9585")
            self.my_scrollbar = Scrollbar(self.contact_frame,orient = VERTICAL,command = self.canvas.yview)
            self.canvas.configure(yscrollcommand = self.my_scrollbar.set)

            self.my_scrollbar.pack(side = RIGHT,fill = Y)
            self.canvas.pack(side = LEFT)
            self.canvas.create_window((0,0),window = self.dummy_frame,anchor = "nw")
            self.dummy_frame.bind("<Configure>",lambda e:self.canvas.configure(scrollregion = self.canvas.bbox("all"),width = 410,height = 600))
            
            if purpose is None:
                for record in self.records:                
                    self.current = Button(self.dummy_frame,text = f"{record[0]:<15}{record[1]:<15}",anchor = "w",
                    font = "comicsansms 15",padx = 120,pady = 10,bg = next(self.colors),fg = "#DC2C28")
                    self.current.pack(fill = X,anchor = "w")
                    self.current.bind("<Button-1>",self.display_contact_info)
            else:
                for record in self.records:                
                    self.current = Button(self.dummy_frame,text = f"{record[0]:<15}{record[1]:<15}",anchor = "w",
                    font = "comicsansms 15",padx = 120,pady = 10,bg = next(self.colors),fg = "#DC2C28")
                    self.current.pack(fill = X,anchor = "w")
                    self.current.bind("<Button-1>",self.delete_me)

            
        
    def about_us(self):
        self.new_frame = Frame(self,bg = "#FF9585")
        self.new_frame.place(relx = 0,rely = 0,relwidth = 1,relheight = 1)
       
        self.about_header = Label(self.new_frame,bg = "#FF9585",text = "About Us",font = "comicsansms 17 bold",fg = "#008A7A")
        self.about_header.place(relx = 0.5 ,rely = 0,relwidth = 1,relheight = 1/12,anchor = "n")

        with open("about_us.txt","r") as f:
            data = "\n".join(f.read().split("\r\n"))
        self.info_label = Label(self.new_frame,bg = "#E8E66E",fg = "#861BA7",font = "comicsansms 15",borderwidth = 5,
        relief = RIDGE,text = data,padx = 10,pady = 10,anchor = "w")
        self.info_label.place(relx = 1/12,rely = 1/8,relwidth = 5/6,relheight = 5/12)

        self.feedback_label = Label(self.new_frame,bg = "#FF9585",fg = "#008A7A",text = "Your feedback",
        font = "comicsansms 17 bold")
        self.feedback_label.place(relx = 4/12,rely = 7/12,relwidth = 1/3,relheight = 1/12)
        
        self.radio_var = StringVar()
        self.radio_var.set(" ")
    
        self.radio = Radiobutton(self.new_frame,text = "Satisfied,Very useful GUI",value = "yes" ,activeforeground = "#861BA7",
        variable = self.radio_var,anchor = "w",bg = "#FF9585",font = "comicsansms 12",fg = "#861BA7",activebackground = "#FF9585")
        self.radio.place(relx = 1/12,rely = 8/12,relwidth = 5/6,relheight = 1/12)

        self.radio = Radiobutton(self.new_frame,text = "Not Satisfied ,Improve this GUI",value = "no" ,activeforeground = "#861BA7",
        variable = self.radio_var,anchor = "w",bg = "#FF9585",font = "comicsansms 12",fg = "#861BA7",activebackground = "#FF9585")
        self.radio.place(relx = 1/12,rely = 9/12,relwidth = 5/6,relheight = 1/12)

        self.back_button = Button(self.new_frame,text = "Back",font  = "comicsansms 15",bg = "#7434EA",fg = "lime",
        command = self.first_view,borderwidth = 3,activebackground = "#7434EA")
        self.back_button.place(relx = 1/12,rely = 9/12+3/24,relwidth = 1/3,relheight = 1/12)

        self.submit_feedback = Button(self.new_frame,text = "Submit",font = "comicsansms 15",bg = "#7434EA",
        fg = "lime",borderwidth = 3,command = self.submit,activebackground = "#7434EA")
        self.submit_feedback.place(relx = 7/12,rely = 9/12+3/24,relwidth = 1/3,relheight = 1/12)
    
    def submit(self):
        vals = self.radio_var.get()

        if vals == "yes":
            tmsg.showinfo("Thank you","Your valuable response was necessary\nWe are happy to keep you satisfied")
        else:
            tmsg.showinfo("OOPS","Ok ,We will try to improve!")

if __name__ == "__main__":
    window = GUI()
    
    window.first_view()

    window.mainloop()