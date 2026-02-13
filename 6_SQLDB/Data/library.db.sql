BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Borrower" (
	"ID"	INTEGER NOT NULL,
	"FirstName"	TEXT NOT NULL,
	"Surname"	TEXT NOT NULL,
	"Contact"	INTEGER CHECK(typeof("Contact") = 'integer'),
	PRIMARY KEY("ID" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Publisher" (
	"ID"	INTEGER NOT NULL,
	"Name"	TEXT NOT NULL,
	PRIMARY KEY("ID" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Book" (
	"ID"	INTEGER NOT NULL,
	"Title"	TEXT NOT NULL,
	"PublisherID"	INTEGER,
	"Damaged"	INTEGER NOT NULL,
	FOREIGN KEY("PublisherID") REFERENCES "Publisher"("ID"),
	PRIMARY KEY("ID")
);
CREATE TABLE IF NOT EXISTS "Loan" (
	"ID"	INTEGER NOT NULL,
	"BorrowerID"	INTEGER NOT NULL,
	"BookID"	INTEGER NOT NULL,
	"Date Borrowed"	TEXT,
	FOREIGN KEY("BorrowerID") REFERENCES "Borrower"("ID"),
	FOREIGN KEY("BookID") REFERENCES "Book"("ID"),
	PRIMARY KEY("ID" AUTOINCREMENT)
);
INSERT INTO "Borrower" ("ID","FirstName","Surname","Contact") VALUES (1,'Peter','Tan',99299345),
 (2,'Sarah','Lee',81111123),
 (3,'Kumara','Ravi',94456677);
INSERT INTO "Publisher" ("ID","Name") VALUES (1,'NPH'),
 (2,'Unpop'),
 (3,'Appleson'),
 (4,'Squirrel'),
 (5,'Yellow Flame'),
 (6,'ZeYuCo');
INSERT INTO "Book" ("ID","Title","PublisherID","Damaged") VALUES (1,'The Lone Gatsby',5,0),
 (2,'A Winter’s Slumber',4,1),
 (3,'Life of Pie',4,0),
 (4,'A Brief History Of Primates',3,0),
 (5,'To Praise a Mocking Bird',2,0),
 (6,'The Catcher in the Eye',1,1),
 (123,'H2 Computing Ten Year Series',NULL,0),
 (124,'H2 Maths 100 Years Series',NULL,0);
INSERT INTO "Loan" ("ID","BorrowerID","BookID","Date Borrowed") VALUES (1,3,2,'20180220'),
 (2,3,1,'20171215'),
 (3,2,3,'20171231'),
 (4,1,5,'20180111');
COMMIT;
