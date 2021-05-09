// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from my_robot_interfaces:srv/InterPol.idl
// generated code does not contain a copyright notice

#ifndef MY_ROBOT_INTERFACES__SRV__DETAIL__INTER_POL__STRUCT_H_
#define MY_ROBOT_INTERFACES__SRV__DETAIL__INTER_POL__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'velocity'
#include "rosidl_runtime_c/string.h"

// Struct defined in srv/InterPol in the package my_robot_interfaces.
typedef struct my_robot_interfaces__srv__InterPol_Request
{
  double shoulder;
  double elbow;
  double wrist;
  double time;
  rosidl_runtime_c__String velocity;
} my_robot_interfaces__srv__InterPol_Request;

// Struct for a sequence of my_robot_interfaces__srv__InterPol_Request.
typedef struct my_robot_interfaces__srv__InterPol_Request__Sequence
{
  my_robot_interfaces__srv__InterPol_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} my_robot_interfaces__srv__InterPol_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'description'
// already included above
// #include "rosidl_runtime_c/string.h"

// Struct defined in srv/InterPol in the package my_robot_interfaces.
typedef struct my_robot_interfaces__srv__InterPol_Response
{
  bool success;
  rosidl_runtime_c__String description;
} my_robot_interfaces__srv__InterPol_Response;

// Struct for a sequence of my_robot_interfaces__srv__InterPol_Response.
typedef struct my_robot_interfaces__srv__InterPol_Response__Sequence
{
  my_robot_interfaces__srv__InterPol_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} my_robot_interfaces__srv__InterPol_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MY_ROBOT_INTERFACES__SRV__DETAIL__INTER_POL__STRUCT_H_
