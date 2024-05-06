USE lexicon;

CREATE TABLE City (
  CityId INT PRIMARY KEY,
  CityName CHAR(50)
);

CREATE TABLE Building (
  BuildingId INT PRIMARY KEY,
  CityId INT,
  Floors INT,
  FOREIGN KEY (CityId) REFERENCES City(CityId)
);

CREATE TABLE ElevatorType (
  ElevatorTypeId INT PRIMARY KEY,
  TypeName CHAR(50)
);

CREATE TABLE ElevatorModel (
  ElevatorModelId INT PRIMARY KEY,
  ModelName CHAR(50),
  Speed INT,
  ElevatorTypeId INT,
  FOREIGN KEY (ElevatorTypeId) REFERENCES ElevatorType(ElevatorTypeId)
);

CREATE TABLE Elevator (
  ElevatorId INT PRIMARY KEY,
  ElevatorModelId INT,
  BuildingId INT,
  InstallationDate Date,
  FOREIGN KEY (BuildingId) REFERENCES Building(BuildingId),
  FOREIGN KEY (ElevatorModelId) REFERENCES ElevatorModel(ElevatorModelId)
);

CREATE TABLE ServiceStatus (
  ServiceStatusId INT PRIMARY KEY,
  StatusDescription CHAR(50)
);

CREATE TABLE EmployeeStatus (
  EmployeeStatusId INT PRIMARY KEY,
  StatusDescription CHAR(50)
);

CREATE TABLE Technician (
  EmployeeId INT PRIMARY KEY,
  FirstName CHAR(50),
  LastName CHAR(50),
  EmailAddress CHAR(100),
  AnnualSalary INT,
  SpecialSkill Char(50),
  EmployeeStatusId INT,
  FOREIGN KEY (EmployeeStatusId) REFERENCES EmployeeStatus(EmployeeStatusId)
);

CREATE TABLE ServiceActivity (
  ServiceActivityId INT PRIMARY KEY,
  EmployeeId INT,
  ElevatorId INT,
  ServiceDateTime DATE,
  ServiceDescription CHAR(255),
  ServiceStatusId INT,
  FOREIGN KEY (EmployeeId) REFERENCES Technician(EmployeeId),
  FOREIGN KEY (ElevatorId) REFERENCES Elevator(ElevatorId),
  FOREIGN KEY (ServiceStatusId) REFERENCES ServiceStatus(ServiceStatusId)
);
