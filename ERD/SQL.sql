CREATE TABLE "people" (
  "Income Group" VARCHAR(6) NOT NULL,
  "Per Capita GDP" DECIMAL(10,2) NOT NULL,
  "Population (millions)" DECIMAL(10,2) NOT NULL,
  "Human Development Index (HDI)" DECIMAL(10,2) NOT NULL,
  "Life Expectancy" DECIMAL(10,2) NOT NULL
);

CREATE TABLE "land" (
  "Country" VARCHAR(50) NOT NULL,
  "Region" VARCHAR(50) NOT NULL,
  "SDGi" DECIMAL(10,2) NOT NULL,
  "Cropland Footprint" DECIMAL(10,2) NOT NULL,
  "Grazing Footprint" DECIMAL(10,2) NOT NULL,
  "Forest Product Footprint" DECIMAL(10,2) NOT NULL,
  "Carbon Footprint" DECIMAL(10,2) NOT NULL,
  "Fish Footprint" DECIMAL(10,2) NOT NULL,
  "Built up land" DECIMAL(10,2) NOT NULL,
  "Total Ecological Footprint (Consumption)" DECIMAL(10,6) NOT NULL,
  "Cropland" DECIMAL(10,2) NOT NULL,
  "Grazing land" DECIMAL(10,2) NOT NULL,
  "Forest land" DECIMAL(10,2) NOT NULL,
  "Fishing ground" DECIMAL(10,2) NOT NULL,
  "Total biocapacity" DECIMAL(10,2) NOT NULL,
  "Ecological (Deficit) or Reserve" DECIMAL(10,2) NOT NULL,
  "Number of Earths required" DECIMAL(10,2) NOT NULL,
  "Number of Countries required" DECIMAL(10,2) NOT NULL
);

ALTER TABLE "people" ADD FOREIGN KEY ("Population (millions)") REFERENCES "people" ("Income Group");

ALTER TABLE "land" ADD FOREIGN KEY ("Ecological (Deficit) or Reserve") REFERENCES "land" ("Forest land");

ALTER TABLE "land" ADD FOREIGN KEY ("Total Ecological Footprint (Consumption)") REFERENCES "land" ("Number of Earths required");

ALTER TABLE "land" ADD FOREIGN KEY ("SDGi") REFERENCES "land" ("Region");

ALTER TABLE "land" ADD FOREIGN KEY ("SDGi") REFERENCES "people" ("Life Expectancy");

ALTER TABLE "land" ADD FOREIGN KEY ("Region") REFERENCES "people" ("Per Capita GDP");

ALTER TABLE "people" ADD FOREIGN KEY ("Life Expectancy") REFERENCES "land" ("Cropland Footprint");

ALTER TABLE "land" ADD FOREIGN KEY ("Country") REFERENCES "people" ("Human Development Index (HDI)");

ALTER TABLE "land" ADD FOREIGN KEY ("Fish Footprint") REFERENCES "land" ("Fishing ground");

ALTER TABLE "land" ADD FOREIGN KEY ("Total biocapacity") REFERENCES "people" ("Life Expectancy");
