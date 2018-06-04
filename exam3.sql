CREATE TABLE "carpet" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL,
"quantity" integer NOT NULL, "reorder_quantity" integer NOT NULL, "date_created" datetime NOT NULL,
"date_modified" datetime NOT NULL);

CREATE TABLE "carpet_cut" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "remaining_length" integer NOT NULL,
"remaining_width" integer NOT NULL, "is_empty" bool NOT NULL, "first_cut_date" date NOT NULL,
"date_created" datetime NOT NULL, "date_modified" datetime NOT NULL,
"carpet_id" integer NOT NULL REFERENCES "carpet" ("id") DEFERRABLE INITIALLY DEFERRED);

CREATE TABLE "carpet_order" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "order_date" datetime NOT NULL,
"delivery_date" datetime NOT NULL, "date_created" datetime NOT NULL, "date_modified" datetime NOT NULL,
"carpet_id" integer NOT NULL REFERENCES "carpet" ("id") DEFERRABLE INITIALLY DEFERRED);

CREATE TABLE "carpet_order_line" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "quantity" integer NOT NULL,
"length" integer NOT NULL, "width" integer NOT NULL, "is_served" bool NOT NULL, "date_created" datetime NOT NULL,
"date_modified" datetime NOT NULL,
"order_id" integer NOT NULL REFERENCES "carpet_order" ("id") DEFERRABLE INITIALLY DEFERRED);

CREATE TABLE "carpet_type" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL,
"date_created" datetime NOT NULL, "date_modified" datetime NOT NULL);

CREATE TABLE "restock_order" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "quantity" integer NOT NULL,
"is_delivered" bool NOT NULL, "delivery_date" datetime NOT NULL, "date_created" datetime NOT NULL,
"date_modified" datetime NOT NULL,
"carpet_id" integer NOT NULL REFERENCES "carpet" ("id") DEFERRABLE INITIALLY DEFERRED);


1. Restock carpet rolls

- The system should have a worker that automatically checks if the quantity remaining for each carpet
has already reached its reorder point.

- Since there are different carpet types and demands for each, they should have different reorder
points rather than a universal one.

2. Cut from a roll of carpet

- If there are just enough area to serve the orders, then those will be cut, and deducted to
the remaining_length and remaining_width on the CarpetCut table or Carpet depending on which carpet shall be served.

- Once both remaining_length and remaining_width reached 0, then the record will be flagged as
is_empty. This is to ensure that they'll be skipped for determining which carpet to cut to.

3. Select which roll of carpet to cut from

- The orders that shall be served first are those orders with 100 x 100 area. They will directly be deducted
on the Carpet table.

- Any order that has lesser than 100 x 100 will be served via CarpetCut table.
The system will query based on area first, then will sort it by first_cut_date.

- If there are lesser or no available already cutted carpets that can serve the needs,
then we'll deduct a quantity/quantities (depending on the need) from Carpet table.

- The remains from the said cut will be then recorded to the CarpetCut table along with the necessary info.
