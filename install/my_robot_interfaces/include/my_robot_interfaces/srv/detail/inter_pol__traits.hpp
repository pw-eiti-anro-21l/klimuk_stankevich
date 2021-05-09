// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from my_robot_interfaces:srv/InterPol.idl
// generated code does not contain a copyright notice

#ifndef MY_ROBOT_INTERFACES__SRV__DETAIL__INTER_POL__TRAITS_HPP_
#define MY_ROBOT_INTERFACES__SRV__DETAIL__INTER_POL__TRAITS_HPP_

#include "my_robot_interfaces/srv/detail/inter_pol__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<my_robot_interfaces::srv::InterPol_Request>()
{
  return "my_robot_interfaces::srv::InterPol_Request";
}

template<>
inline const char * name<my_robot_interfaces::srv::InterPol_Request>()
{
  return "my_robot_interfaces/srv/InterPol_Request";
}

template<>
struct has_fixed_size<my_robot_interfaces::srv::InterPol_Request>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<my_robot_interfaces::srv::InterPol_Request>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<my_robot_interfaces::srv::InterPol_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<my_robot_interfaces::srv::InterPol_Response>()
{
  return "my_robot_interfaces::srv::InterPol_Response";
}

template<>
inline const char * name<my_robot_interfaces::srv::InterPol_Response>()
{
  return "my_robot_interfaces/srv/InterPol_Response";
}

template<>
struct has_fixed_size<my_robot_interfaces::srv::InterPol_Response>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<my_robot_interfaces::srv::InterPol_Response>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<my_robot_interfaces::srv::InterPol_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<my_robot_interfaces::srv::InterPol>()
{
  return "my_robot_interfaces::srv::InterPol";
}

template<>
inline const char * name<my_robot_interfaces::srv::InterPol>()
{
  return "my_robot_interfaces/srv/InterPol";
}

template<>
struct has_fixed_size<my_robot_interfaces::srv::InterPol>
  : std::integral_constant<
    bool,
    has_fixed_size<my_robot_interfaces::srv::InterPol_Request>::value &&
    has_fixed_size<my_robot_interfaces::srv::InterPol_Response>::value
  >
{
};

template<>
struct has_bounded_size<my_robot_interfaces::srv::InterPol>
  : std::integral_constant<
    bool,
    has_bounded_size<my_robot_interfaces::srv::InterPol_Request>::value &&
    has_bounded_size<my_robot_interfaces::srv::InterPol_Response>::value
  >
{
};

template<>
struct is_service<my_robot_interfaces::srv::InterPol>
  : std::true_type
{
};

template<>
struct is_service_request<my_robot_interfaces::srv::InterPol_Request>
  : std::true_type
{
};

template<>
struct is_service_response<my_robot_interfaces::srv::InterPol_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // MY_ROBOT_INTERFACES__SRV__DETAIL__INTER_POL__TRAITS_HPP_
