typedef struct imu{
  double x;
  double y;
  double z;
  double vx;
  double vy;
  double vz;
  double ax;
  double ay;
  double az;
  double compx;
  double compy;
  double compz;
}__attribute__((packed)) imu_t;

typedef struct motor{
  double pos;
  double velos;
  double acc;
}__attribute__((packed)) motor_t;

typedef struct state {
  double time;
  imu_t imu;
  motor_t motor[2];
}__attribute__((packed)) state_t;

