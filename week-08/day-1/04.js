// Create a constructor for creating Aircrafts,
// and one for creating Carriers,
// based on the specification in the python exam: https://github.com/greenfox-academy/zerda-exam-python-retake

function Aircrafts (type) {
  this.type = type;
  this.ammo = 0;
  this.baseDamage = 0;
  this.maxAmmo = 0;
  this.allDamage = this.maxAmmo * this.baseDamage;

  if (this.type === 'F16') {
    this.baseDamage = 30;
    this.maxAmmo = 8;
  } else if (this.type === 'F35') {
    this.baseDamage = 50;
    this.maxAmmo = 12;
  };
};

Aircrafts.prototype.fight = function () {
  this.allDamage = this.ammo * this.baseDamage;
  this.ammo -= this.ammo;
  return this.allDamage
};

Aircrafts.prototype.refill = function (pcs) {
  this.ammo += pcs;
  if (this.ammo > this.maxAmmo) {
    console.log('You refilled to much ammo, ' + (this.ammo - this.maxAmmo) + ' ammo returned to shop.');
  };
  this.allDamage = this.ammo * this.baseDamage;
};

Aircrafts.prototype.log = function () {
  console.log('Type ' + this.type + ', Base Damage: ' + this.baseDamage + ', All Damage:' + this.allDamage);
};

var articsoka = new Aircrafts('F16');
articsoka.refill(8)
articsoka.log();
articsoka.fight()
articsoka.log();

// CARRIER PART!

function Carrier () {
  this.health = 3000;
  this.ammoStorage = 2300;
  this.aircrafts = 0;
  this.allDamage = 0
  this.aircraftsList = [];
}

Carrier.prototype.addAircraft = function (aircraft) {
  this.aircrafts += 1;
  this.aircraftsList.push(aircraft);
}

Carrier.prototype.fillAll = function () {
  for (var i = 0; i < this.aircraftsList.length; i++) {
    var counter = 0
    counter += (this.aircraftsList[i].maxAmmo - this.aircraftsList[i].ammo)
    this.aircraftsList[i].ammo = this.aircraftsList[i].maxAmmo
    this.allDamage += this.aircraftsList[i].maxAmmo * this.aircraftsList[i].baseDamage
    this.ammoStorage -= counter
  }
}

Carrier.prototype.fightAll = function () {
  for (var i = 0; i < this.aircraftsList; i++) {
    var counter = 0
    counter += this.aircraftsList[i].ammo * this.aircraftsList[i].baseDamage
    this.allDamage += counter
  }
}

Carrier.prototype.statusReport = function () {
  if (this.health > 0) {
  console.log('Aircraft count: ' + this.aircrafts + ', Ammo Storage: ' + this.ammoStorage +
', Total Damage: ' + this.allDamage + ', Health remaining: ' + this.health + '\n Artifacts:')
  for (var n = 0; n < this.aircraftsList.length; n++) {
    console.log('Type ' + this.aircraftsList[n].type + ', Ammo: ' + this.aircraftsList[n].ammo + ', Base Damage: ' + this.aircraftsList[n].baseDamage +
  ', All Damage: ' + this.aircraftsList[n].allDamage)
    }
  } else {
    console.log('It\'s dead Jim.')
  }
}

var banyahajo = new Carrier()
banyahajo.addAircraft(articsoka)
banyahajo.fillAll()
banyahajo.statusReport()
