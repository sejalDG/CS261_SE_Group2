BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "strikePrice" (
	"product"	TEXT NOT NULL,
	"buyer"	TEXT NOT NULL,
	"seller"	TEXT NOT NULL,
	"mean"	REAL NOT NULL,
	"standard_deviation"	REAL NOT NULL,
	"min"	REAL NOT NULL,
	"max"	REAL NOT NULL,
	"count"	INTEGER NOT NULL DEFAULT 0,
	PRIMARY KEY("product","buyer","seller")
);
CREATE TABLE IF NOT EXISTS "underlyingPrice" (
	"product"	TEXT NOT NULL,
	"buyer"	TEXT NOT NULL,
	"seller"	TEXT NOT NULL,
	"mean"	REAL NOT NULL,
	"standard_deviation"	REAL NOT NULL,
	"min"	REAL NOT NULL,
	"max"	REAL NOT NULL,
	"count"	INTEGER NOT NULL DEFAULT 0,
	PRIMARY KEY("seller","buyer","product")
);
CREATE TABLE IF NOT EXISTS "quantityEstimate" (
	"product"	TEXT NOT NULL,
	"buyer"	TEXT NOT NULL,
	"seller"	TEXT NOT NULL,
	"mean"	REAL NOT NULL,
	"standard_deviation"	REAL NOT NULL,
	"min"	REAL NOT NULL,
	"max"	REAL NOT NULL,
	"count"	INTEGER NOT NULL,
	PRIMARY KEY("product","buyer","seller")
);
CREATE TABLE IF NOT EXISTS "notionalAmount" (
	"product"	TEXT NOT NULL,
	"buyer"	TEXT NOT NULL,
	"seller"	TEXT NOT NULL,
	"average"	REAL NOT NULL,
	"standard_deviation"	REAL NOT NULL,
	"min"	REAL NOT NULL,
	"max"	REAL NOT NULL,
	"count"	INTEGER NOT NULL DEFAULT 0,
	PRIMARY KEY("seller","buyer","product")
);
CREATE TABLE IF NOT EXISTS "currencyValues" (
	"date"	TEXT NOT NULL,
	"currency"	TEXT NOT NULL,
	"valueInUSD"	REAL NOT NULL,
	PRIMARY KEY("currency")
);
CREATE TABLE IF NOT EXISTS "productPrices" (
	"date"	TEXT NOT NULL,
	"product"	TEXT NOT NULL,
	"marketPrice"	REAL NOT NULL DEFAULT 0,
	PRIMARY KEY("product")
);
CREATE TABLE IF NOT EXISTS "stockPrices" (
	"date"	TEXT NOT NULL,
	"companyID"	TEXT NOT NULL,
	"stockPrice"	REAL NOT NULL DEFAULT 0,
	PRIMARY KEY("companyID")
);
CREATE TABLE IF NOT EXISTS "derivativeTrades" (
	"dateOfTrade"	TEXT NOT NULL,
	"tradeID"	TEXT NOT NULL,
	"product"	TEXT NOT NULL,
	"buyingParty"	TEXT NOT NULL,
	"sellingParty"	TEXT NOT NULL,
	"notionalAmount"	REAL NOT NULL DEFAULT 0,
	"quantity"	INTEGER NOT NULL,
	"maturityDate"	TEXT NOT NULL,
	"underlyingPrice"	REAL NOT NULL DEFAULT 0,
	"underylingCurrency"	TEXT NOT NULL,
	"strikePrice"	REAL NOT NULL DEFAULT 0,
	PRIMARY KEY("tradeID")
);
COMMIT;
