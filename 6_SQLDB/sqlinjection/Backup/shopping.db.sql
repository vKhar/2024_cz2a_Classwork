BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "customer" (
	"id"	CHAR(4) CHECK(length("id") = 4),
	"name"	VARCHAR(32) NOT NULL,
	"gender"	CHAR(1) CHECK("gender" = 'M' OR "gender" = 'F'),
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "item" (
	"id"	CHAR(6) CHECK(length("id") = 6),
	"name"	VARCHAR(32) NOT NULL,
	"price"	NUMERIC CHECK("price" >= 0),
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "shop_order" (
	"id"	CHAR(7),
	"customerID"	CHAR(4),
	"itemID"	CHAR(6),
	"quantity"	INTEGER CHECK("quantity" > 0),
	"address"	VARCHAR(128) NOT NULL,
	"order_date"	DATE NOT NULL,
	"shipping_date"	DATE CHECK("shipping_date" >= "order_date" OR "shipping_date" IS NULL),
	PRIMARY KEY("id"),
	FOREIGN KEY("itemID") REFERENCES "item"("id"),
	FOREIGN KEY("customerID") REFERENCES "customer"("id")
);
CREATE TABLE IF NOT EXISTS "Login" (
	"id"	TEXT,
	"password"	TEXT CHECK(length("password") > 7),
	PRIMARY KEY("id")
);
INSERT INTO "customer" ("id","name","gender") VALUES ('123X','Josef Segal','M'),
 ('X321','Benji Roberts','M'),
 ('456Y','Kenny Monroe','M'),
 ('Y654','Jessica Powers','F'),
 ('789T','Rosa Lawrence','F'),
 ('T987','Walter Hunter','M'),
 ('1234','Hello','M');
INSERT INTO "item" ("id","name","price") VALUES ('XER342','Vaccum Cleaner',200),
 ('XY3K19','Mini Fridge',500),
 ('X2Z34T','Electric Toothbrush',12),
 ('XFG123','Free Gift',0),
 ('XTP456','Toilet Paper',2),
 ('XCD789','Call of Duty',50),
 ('XFB666','Fake Bag',20000);
INSERT INTO "shop_order" ("id","customerID","itemID","quantity","address","order_date","shipping_date") VALUES ('123123E','123X','XER342',1,'5001 Summer Street','2013-02-14','2013-02-14'),
 ('456456W','456Y','XY3K19',3,'2000 Winter Road','2015-10-02','2015-10-02'),
 ('789789G','789T','X2Z34T',2,'666 Spring Avenue','2016-06-06','2016-06-06'),
 ('123123F','123X','XFG123',1000,'5001 Summer Street','2017-01-10','2017-01-10'),
 ('123123G','123X','XTP456',20,'5001 Summer Street','2017-01-15','2017-01-15'),
 ('123123H','123X','XTP456',50,'5001 Summer Street','2017-02-04',NULL),
 ('123123I','123X','X2Z34T',2,'5001 Summer Street','2017-01-20','2017-01-20'),
 ('456456X','456Y','XCD789',1,'2000 Winter Road','2017-01-29','2017-01-30'),
 ('456456Y','456Y','XER342',1,'2000 Winter Road','2017-02-01',NULL),
 ('789789H','789T','XFG123',5,'666 Spring Avenue','2017-01-01','2017-01-01'),
 ('789789I','789T','XTP456',20,'666 Spring Avenue','2017-02-02','2017-02-03'),
 ('789789K','789T','XY3K19',1,'666 Spring Avenue','2017-01-02','2017-01-03'),
 ('789789L','789T','XY3K19',5,'666 Spring Avenue','2017-01-08','2017-03-10'),
 ('321321S','X321','XER342',1,'2 Autumn Park','2017-01-13','2017-01-14'),
 ('321321T','X321','XCD789',20,'2 Autumn Park','2017-01-13','2017-01-14'),
 ('321321U','X321','XFG123',150,'2 Autumn Park','2017-01-13','2017-01-14'),
 ('654654K','Y654','X2Z34T',5,'666 Spring Avenue','2017-02-02','2017-02-02'),
 ('654654L','Y654','XER342',30,'666 Spring Avenue','2017-01-21','2017-01-22'),
 ('654654M','Y654','XCD789',12,'666 Spring Avenue','2017-02-02','2017-02-10');
INSERT INTO "Login" ("id","password") VALUES ('apple','123456789'),
 ('orange','987654321'),
 ('mango','111111111111'),
 ('123','222222222');
COMMIT;
