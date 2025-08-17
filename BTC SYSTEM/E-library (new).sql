create table Publisher (
PublisherID nvarchar(50) Primary Key,
PublisherName nvarchar(50),
PublisherEmail nvarchar(50),
PublisherPhone nvarchar(50),
PublisherAddress nvarchar(100)
);

Insert Into Publisher (PublisherID, PublisherName, PublisherEmail, PublisherPhone, PublisherAddress)
Values
('P01','Tor Books', 'TorBooks@gmail.com', '018-2854-8160','Equitable Building, New York City'),
('P02','Penguin Random House', 'PenguinRH@gmail.com', '013-098-9813','Level 1, Tower 2A, Avenue 5 Bangsar South No. 8 Jalan Kerinchi 59200 Kuala Lumpur, Malaysia'),
('P03','Simon & Schuster', 'Simon&S@gmail,com', '607-269-7499','Flatiron Building, New York'),
('P04','Hachette Book Group',  'HachetteBG@gmail.com', '212-364-1100','1290 Avenue of the Americas Fl 4, New York, New York, 10104, United States'),
('P005','HarpenCollins Publishers', 'HarpenCollins@gmail.com','716-209-9732','195 Broadway. New York, NY 10007.')

create table Member(
MemberID nvarchar(50) Primary Key,
MemberName nvarchar(50),
Gender nvarchar(50),
MemberEmail nvarchar(50),
MemberPhone nvarchar(50),
State nvarchar(50),
Status nvarchar(50)
);
Insert Into Member
(MemberID,MemberName,Gender,MemberEmail,MemberPhone,State,Status)
Values
('M001','Chris','Male','Chris@gmail.com','013-567-9988','Johor','Active'),
('M002','Sharifah','Female','Sharifah45@gmail.com','011-876-0622','Perak','Active'),
('M003','Esther','Female','Esther620@gmail.com','013-476-0987','Selangor','Active'),
('M004','Alan Tan','Male', 'Alan789@gmail.com','016-476-0721','Selangor','Unactive'),
('M005','Christina','Female','Ctn242@gmail.com','011-585-0141','Selangor','Active'),
('M006','Joseph Wong','Male','JW4813@gmail.com','012-388-8888','Sabah','Active'),
('M007','Ash Thian','Male','tlm9@gmail.com','017-964-9981','Selangor','Active'),
('M008','Wong Juei Tien','Male','WJT@gmail.com','016-666-6666','Negeri Sembilan','Active'),
('M009','Jacky Siaw','Male','JS012@gmail.com','015-999-9899','Pahang','Unactive'),
('M010','Jade Chan','Female','jcn@gmail.com','012-617-7777','Selangor','Unactive')

create table Book(
ISBN nvarchar(50) Primary Key,
Title nvarchar(100),
Author nvarchar(50),
Genre nvarchar(50),
CategoryName nvarchar(50),
BookDescription nvarchar(100),
PublisherID nvarchar(50),
Foreign Key (PublisherID) references Publisher(PublisherID)
);
Insert Into Book
(ISBN,Title,Author,Genre,CategoryName,BookDescription,PublisherID)
Values
('BN1004','A TIME TO KILL','JOHN GRISHAM','Legal thriller','yellow-tagged','King of Jerusalem who relates and analyses events in his own life','P01'),
('BN9998','VILE BODIES','EVELYN WAUGH','Novel, satire','red-tagged','change our vile body and that it may be fashioned like unto his glorious body','P02'),
('BN10','MOAB IS MY WASHPOT','STEPHEN FRY','Autobiography','green-tagged','kingdom of Jordan which was often warring against the Israelites needed to be overcome','P01'),
('BN7741','Python Crash Course 3rd Edition describe A Hands On Project Based Introduction to Programming','Eric Matthes','Programming','green-tagged','making it the ultimate launchpad for beginners to start their engines and code in Python 3','P04'),
('BN1','To Live','Yu Hua','Literary Fiction','green-tagged','Delves deep into the human experience highlight the enduring spirit of individuals facing adversity','P03'),
('BN164','1984','George Orwell','Dystopian Fiction','red-tagged','set in a totalitarian society ruled by the Party and its leader','P04'),
('BN237','Final Fantasy Part 1','Quintilius Demarcus 3rd','Fantasy','green-tagged','Mighty black warrior in a quest to save the last prince and to overcome his fears in Fantasy Land','P02'),
('BN515','Intoduction to Linear Algebra','Gilbert Strang','Mathematics','red-tagged','comprehensive and widely used textbook that introduces the fundamental concepts of linear algebra','P02'),
('BN666','A Brief History of Time','Stephen Hawking','Popular Science','yellow-tagged','explores the fundamental concepts of astrophysics and cosmology','P01'),
('BN987','To Kill a Mockingbird','Harpen Lee','Legal Drama','red-tagged','Beautifully illustrates the power of moral and the importance of standing up for what is right','P04'),
('BN999','The Name of the Wind','Patrick Rothfuss','Fantasy','red-tagged','follow the story of Kvothe, a gifted musician and magician','P01'),
('BN888','Mistborn: The Final Empire','Brandon Sanderson','Fantasy','yellow-tagged',' street thief named Vin discovers her unique magical talents','P02'),
('BN777','The Firm','JOHN GRISHAM','Legal Thriller','red-tagged','Mitch must navigate a dangerous web of deception to protect his life and his family','P01'),
('BN799','The Pelican Brief','JOHN GRISHAM','Legal Thriller','red-tagged','motives behind the assassination of two Supreme Court justices','P01'),
('BN801','Brideshead Revisited','Evelyn Waugh','Literary Fiction','green tagged',' It delves into themes of love, religion, and the decline of the British aristocracy','P02'),
('BN890','Scoop','Evelyn Waugh','Satirical Fiction','yellow tagged','a nature writer mistakenly sent to cover a war in the fictional African country of Ishmaelia','P02')




create table Category(
CategoryID nvarchar(50) Primary Key,
CategoryName nvarchar(50),
CategoryPrice decimal(10,2)
);

Insert Into Category
(CategoryID,CategoryName,CategoryPrice)
Values
('C001','yellow-tagged','1.50'),
('C002','red-tagged','1.00'),
('C003','Green-tagged','0.50')

create table Loan(
LoanID nvarchar(50) Primary Key,
MemberID nvarchar(50),
ISBN nvarchar(50),
LoanDate date,
DueDate date,
LoanDueDate decimal(31,0),
ReturnedDate date,
CategoryID nvarchar(50),
Foreign Key (MemberID) references Member(MemberID),
Foreign Key (ISBN) references Book(ISBN),
Foreign Key (CategoryID) references Category(CategoryID)
);

Insert Into Loan
(LoanID,MemberID,ISBN,LoanDate,DueDate,LoanDueDate,ReturnedDate,CategoryID)
Values
('L002','M005','BN237','15/Jan/2022','19/Jan/2022',NULL,'19/Jan/2022','C003'),
('L020','M001','BN1004','2/July/2022','16/July/2022',NULL,'12/July/2022','C001'),
('L100','M002','BN9998','5/Aug/2022','19/Aug/2022','1','20/Aug/2022','C002'),
('L101','M002','BN237','5/Aug/2022','19/Aug/2022','1','20/Aug/2022','C003'),
('L875','M003','BN10','3/Aug/2022','17/Aug/2022','6','23/Aug/2022','C003'),
('L876','M003','BN7741','3/Aug/2022','17/Aug/2022','6','23/Aug/2022','C003'),
('L878','M003','BN515','3/Aug/2022','17/Aug/2022','6','23/Aug/2022','C002'),
('L901','M007','BN666','19/Nov/2022','3/Dec/2022','7','10/Dec/2022','C001'),
('L902','M007','BN987','19/Nov/2022','3/Dec/2022','7','10/Dec/2022','C002'),
('L999','M005','BN10','1/Jan/2023','15/Jan/2023','4','19/Jan/2023','C003'),
('L1010','M008','BN1','13/Feb/2023','27/Feb/2023','1','28/Feb/2023','C003'),
('L1030','M006','BN164','29/Mar/2023','12/Apr/2023','5','17/Apr/2023','C002'),
('L1050','M001','BN237','4/Apr/2023','18/Apr/2023',NULL,'16/Apr/2023','C003'),
('L1077','M005','BN666','8/May/2023','22/May/2023','4','26/May/2023','C001'),
('L1078','M005','BN1004','8/May/2023','22/May/2023','4','26/May/2023','C001'),
('L1079','M005','BN164','8/May/2023','22/May/2023','4','26/May/2023','C002'),
('L1098','M003','BN1','6/Jun/2023','20/Jun/2023','7','27/Jun/2023','C003'),
('L1099','M003','BN9998','6/Jun/2023','20/Jun/2023','7','27/Jun/2023','C002'),
('L1140','M007','BN164','10/July/2023','24/July/2023','9','2/Aug/2023','C002'),
('L1190','M008','BN1004','1/Aug/2023','15/Aug/2023','2','17/Aug/2023','C001')





create table Reservation(
ReservationID nvarchar(50),
MemberID nvarchar(50),
ISBN nvarchar(50),
ReservationDate date,
NotificationDate date,
Foreign Key (MemberID) references Member(MemberID),
Foreign Key (ISBN) references Book(ISBN)
);

Insert Into Reservation
(ReservationID,MemberID,ISBN,ReservationDate,NotificationDate)
Values
('R002','M005','BN237','15/Jan/2022','12/Jan/2022'),
('R020','M001','BN1004','2/July/2022','29/Jun/2022'),
('R098','M002','BN9998','5/Aug/2022','2/Aug/2022'),
('R098','M002','BN237','5/Aug/2022','2/Aug/2022'),
('R200','M003','BN10','3/Aug/2022','31/July/2022'),
('R200','M003','BN7741','3/Aug/2022','31/July/2022'),
('R200','M003','BN515','3/Aug/2022','31/July/2022'),
('R505','M007','BN666','19/Nov/2022','16/Nov/2022'),
('R505','M007','BN987','19/Nov/2022','16/Nov/2022'),
('R566','M005','BN10','1/Jan/2023','29/Dec/2022'),
('R1010','M008','BN1','13/Feb/2023','10/Feb/2023'),
('R1030','M006','BN164','29/Mar/2023','26/Mar/2023'),
('R1050','M001','BN237','4/Apr/2023','1/Apr/2023'),
('R1077','M005','BN666','8/May/2023','5/May/2023'),
('R1078','M005','BN1004','8/May/2023','5/May/2023'),
('R1079','M005','BN164','8/May/2023','5/May/2023'),
('R1098','M003','BN1','6/Jun/2023','3/Jun/2023'),
('R1099','M003','BN9998','6/Jun/2023','3/Jun/2023'),
('R1140','M007','BN164','10/July/2023','7/July/2023'),
('R1190','M008','BN1004','1/Aug/2023','29/July/2023')

Select*from Member
Select*from Book
Select*from Category
Select*from Loan
Select*from Reservation
Select*from Publisher