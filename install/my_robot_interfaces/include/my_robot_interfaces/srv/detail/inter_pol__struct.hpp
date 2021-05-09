// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from my_robot_interfaces:srv/InterPol.idl
// generated code does not contain a copyright notice

#ifndef MY_ROBOT_INTERFACES__SRV__DETAIL__INTER_POL__STRUCT_HPP_
#define MY_ROBOT_INTERFACES__SRV__DETAIL__INTER_POL__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__my_robot_interfaces__srv__InterPol_Request __attribute__((deprecated))
#else
# define DEPRECATED__my_robot_interfaces__srv__InterPol_Request __declspec(deprecated)
#endif

namespace my_robot_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct InterPol_Request_
{
  using Type = InterPol_Request_<ContainerAllocator>;

  explicit InterPol_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->shoulder = 0.0;
      this->elbow = 0.0;
      this->wrist = 0.0;
      this->time = 0.0;
      this->velocity = "";
    }
  }

  explicit InterPol_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : velocity(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->shoulder = 0.0;
      this->elbow = 0.0;
      this->wrist = 0.0;
      this->time = 0.0;
      this->velocity = "";
    }
  }

  // field types and members
  using _shoulder_type =
    double;
  _shoulder_type shoulder;
  using _elbow_type =
    double;
  _elbow_type elbow;
  using _wrist_type =
    double;
  _wrist_type wrist;
  using _time_type =
    double;
  _time_type time;
  using _velocity_type =
    std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>;
  _velocity_type velocity;

  // setters for named parameter idiom
  Type & set__shoulder(
    const double & _arg)
  {
    this->shoulder = _arg;
    return *this;
  }
  Type & set__elbow(
    const double & _arg)
  {
    this->elbow = _arg;
    return *this;
  }
  Type & set__wrist(
    const double & _arg)
  {
    this->wrist = _arg;
    return *this;
  }
  Type & set__time(
    const double & _arg)
  {
    this->time = _arg;
    return *this;
  }
  Type & set__velocity(
    const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other> & _arg)
  {
    this->velocity = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    my_robot_interfaces::srv::InterPol_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const my_robot_interfaces::srv::InterPol_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<my_robot_interfaces::srv::InterPol_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<my_robot_interfaces::srv::InterPol_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      my_robot_interfaces::srv::InterPol_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<my_robot_interfaces::srv::InterPol_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      my_robot_interfaces::srv::InterPol_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<my_robot_interfaces::srv::InterPol_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<my_robot_interfaces::srv::InterPol_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<my_robot_interfaces::srv::InterPol_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__my_robot_interfaces__srv__InterPol_Request
    std::shared_ptr<my_robot_interfaces::srv::InterPol_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__my_robot_interfaces__srv__InterPol_Request
    std::shared_ptr<my_robot_interfaces::srv::InterPol_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const InterPol_Request_ & other) const
  {
    if (this->shoulder != other.shoulder) {
      return false;
    }
    if (this->elbow != other.elbow) {
      return false;
    }
    if (this->wrist != other.wrist) {
      return false;
    }
    if (this->time != other.time) {
      return false;
    }
    if (this->velocity != other.velocity) {
      return false;
    }
    return true;
  }
  bool operator!=(const InterPol_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct InterPol_Request_

// alias to use template instance with default allocator
using InterPol_Request =
  my_robot_interfaces::srv::InterPol_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace my_robot_interfaces


#ifndef _WIN32
# define DEPRECATED__my_robot_interfaces__srv__InterPol_Response __attribute__((deprecated))
#else
# define DEPRECATED__my_robot_interfaces__srv__InterPol_Response __declspec(deprecated)
#endif

namespace my_robot_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct InterPol_Response_
{
  using Type = InterPol_Response_<ContainerAllocator>;

  explicit InterPol_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
      this->description = "";
    }
  }

  explicit InterPol_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : description(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
      this->description = "";
    }
  }

  // field types and members
  using _success_type =
    bool;
  _success_type success;
  using _description_type =
    std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>;
  _description_type description;

  // setters for named parameter idiom
  Type & set__success(
    const bool & _arg)
  {
    this->success = _arg;
    return *this;
  }
  Type & set__description(
    const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other> & _arg)
  {
    this->description = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    my_robot_interfaces::srv::InterPol_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const my_robot_interfaces::srv::InterPol_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<my_robot_interfaces::srv::InterPol_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<my_robot_interfaces::srv::InterPol_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      my_robot_interfaces::srv::InterPol_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<my_robot_interfaces::srv::InterPol_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      my_robot_interfaces::srv::InterPol_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<my_robot_interfaces::srv::InterPol_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<my_robot_interfaces::srv::InterPol_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<my_robot_interfaces::srv::InterPol_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__my_robot_interfaces__srv__InterPol_Response
    std::shared_ptr<my_robot_interfaces::srv::InterPol_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__my_robot_interfaces__srv__InterPol_Response
    std::shared_ptr<my_robot_interfaces::srv::InterPol_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const InterPol_Response_ & other) const
  {
    if (this->success != other.success) {
      return false;
    }
    if (this->description != other.description) {
      return false;
    }
    return true;
  }
  bool operator!=(const InterPol_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct InterPol_Response_

// alias to use template instance with default allocator
using InterPol_Response =
  my_robot_interfaces::srv::InterPol_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace my_robot_interfaces

namespace my_robot_interfaces
{

namespace srv
{

struct InterPol
{
  using Request = my_robot_interfaces::srv::InterPol_Request;
  using Response = my_robot_interfaces::srv::InterPol_Response;
};

}  // namespace srv

}  // namespace my_robot_interfaces

#endif  // MY_ROBOT_INTERFACES__SRV__DETAIL__INTER_POL__STRUCT_HPP_
