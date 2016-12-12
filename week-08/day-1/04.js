// Create a constructor for creating Aircrafts,
// and one for creating Carriers,
// based on the specification in the python exam: https://github.com/greenfox-academy/zerda-exam-python-retake

function Aircrafts (type) {
  this.ammo = 0;
  this.allDamage = 0;
  this.type = type;
  this.baseDamage = 0;
  this.maxAmmo = 0;

  if (this.type === 'F16') {
    this.baseDamage = 30;
    this.maxAmmo = 8;
  } else if (this.type === 'F35') {
    this.baseDamage = 50;
    this.maxAmmo = 12;
  };
};

Aircrafts.prototype.fight = function () {
  this.ammo -= this.ammo;
  this.allDamage = this.ammo * this.baseDamage;
};

Aircrafts.prototype.refill = function (pcs) {
  this.ammo += pcs;
  if (this.ammo > this.maxAmmo) {
    console.log('You refilled to much ammo, ' + (this.ammo - this.maxAmmo) + ' ammo returned to shop.');
  };
};
Aircrafts.prototype.log = function () {
  console.log('Type ' + this.type + ', Base Damage: ' + this.baseDamage + ', All Damage:' + this.allDamage);
};

var articsoka = new Aircrafts('F16');
articsoka.log();
articsoka.refill(10)
// function Carrier () {
//
// }
