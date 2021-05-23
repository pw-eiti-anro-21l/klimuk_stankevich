// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from my_robot_interfaces:srv/InterPol2.idl
// generated code does not contain a copyright notice

#ifndef MY_ROBOT_INTERFACES__SRV__DETAIL__INTER_POL2__STRUCT_HPP_
#define MY_ROBOT_INTERFACES__SRV__DETAIL__INTER_POL2__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__my_robot_interfaces__srv__InterPol2_Request __attribute__((deprecated))
#else
# define DEPRECATED__my_robot_interfaces__srv__InterPol2_Request __declspec(deprecated)
#endif

namespace my_robot_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct InterPol2_Request_
{
  using Type = InterPol2_Request_<ContainerAllocator>;

  explicit InterPol2_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->posx = 0.0;
      this->posy = 0.0;
      this->posz = 0.0;
      this->r = 0.0;
      this->p = 0.0;
      this->y = 0.0;
      this->time = 0.0;
      this->shape = "";
    }
  }

  explicit InterPol2_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : shape(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->posx = 0.0;
      this->posy = 0.0;
      this->posz = 0.0;
      this->r = 0.0;
      this->p = 0.0;
      this->y = 0.0;
      this->time = 0.0;
      this->shape = "";
    }
  }

  // field types and members
  using _posx_type =
    double;
  _posx_type posx;
  using _posy_type =
    double;
  _posy_type posy;
  using _posz_type =
    double;
  _posz_type posz;
  using _r_type =
    double;
  _r_type r;
  using _p_type =
    double;
  _p_type p;
  using _y_type =
    double;
  _y_type y;
  using _time_type =
    double;
  _time_type time;
  using _shape_type =
    std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>;
  _shape_type shape;

  // setters for named parameter idiom
  Type & set__posx(
    const double & _arg)
  {
    this->posx = _arg;
    return *this;
  }
  Type & set__posy(
    const double & _arg)
  {
    this->posy = _arg;
    return *this;
  }
  Type & set__posz(
    const double & _arg)
  {
    this->posz = _arg;
    return *this;
  }
  Type & set__r(
    const double & _arg)
  {
    this->r = _arg;
    return *this;
  }
  Type & set__p(
    const double & _arg)
  {
    this->p = _arg;
    return *this;
  }
  Type & set__y(
    const double & _arg)
  {
    this->y = _arg;
    return *this;
  }
  Type & set__time(
    const double & _arg)
  {
    this->time = _arg;
    return *this;
  }
  Type & set__shape(
    const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other> & _arg)
  {
    this->shape = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    my_robot_interfaces::srv::InterPol2_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const my_robot_interfaces::srv::InterPol2_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<my_robot_interfaces::srv::InterPol2_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<my_robot_interfaces::srv::InterPol2_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      my_robot_interfaces::srv::InterPol2_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<my_robot_interfaces::srv::InterPol2_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      my_robot_interfaces::srv::InterPol2_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<my_robot_interfaces::srv::InterPol2_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<my_robot_interfaces::srv::InterPol2_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<my_robot_interfaces::srv::InterPol2_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__my_robot_interfaces__srv__InterPol2_Request
    std::shared_ptr<my_robot_interfaces::srv::InterPol2_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__my_robot_interfaces__srv__InterPol2_Request
    std::shared_ptr<my_robot_interfaces::srv::InterPol2_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const InterPol2_Request_ & other) const
  {
    if (this->posx != other.posx) {
      return false;
    }
    if (this->posy != other.posy) {
      return false;
    }
    if (this->posz != other.posz) {
      return false;
    }
    if (this->r != other.r) {
      return false;
    }
    if (this->p != other.p) {
      return false;
    }
    if (this->y != other.y) {
      return false;
    }
    if (this->time != other.time) {
      return false;
    }
    if (this->shape != other.shape) {
      return false;
    }
    return true;
  }
  bool operator!=(const InterPol2_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct InterPol2_Request_

// alias to use template instance with default allocator
using InterPol2_Request =
  my_robot_interfaces::srv::InterPol2_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace my_robot_interfaces


#ifndef _WIN32
# define DEPRECATED__my_robot_interfaces__srv__InterPol2_Response __attribute__((deprecated))
#else
# define DEPRECATED__my_robot_interfaces__srv__InterPol2_Response __declspec(deprecated)
#endif

namespace my_robot_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct InterPol2_Response_
{
  using Type = InterPol2_Response_<ContainerAllocator>;

  explicit InterPol2_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
      this->description = "";
    }
  }

  explicit InterPol2_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
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
    my_robot_interfaces::srv::InterPol2_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const my_robot_interfaces::srv::InterPol2_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<my_robot_interfaces::srv::InterPol2_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<my_robot_interfaces::srv::InterPol2_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      my_robot_interfaces::srv::InterPol2_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<my_robot_interfaces::srv::InterPol2_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      my_robot_interfaces::srv::InterPol2_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<my_robot_interfaces::srv::InterPol2_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<my_robot_interfaces::srv::InterPol2_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<my_robot_interfaces::srv::InterPol2_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__my_robot_interfaces__srv__InterPol2_Response
    std::shared_ptr<my_robot_interfaces::srv::InterPol2_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__my_robot_interfaces__srv__InterPol2_Response
    std::shared_ptr<my_robot_interfaces::srv::InterPol2_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const InterPol2_Response_ & other) const
  {
    if (this->success != other.success) {
      return false;
    }
    if (this->description != other.description) {
      return false;
    }
    return true;
  }
  bool operator!=(const InterPol2_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct InterPol2_Response_

// alias to use template instance with default allocator
using InterPol2_Response =
  my_robot_interfaces::srv::InterPol2_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace my_robot_interfaces

namespace my_robot_interfaces
{

namespace srv
{

struct InterPol2
{
  using Request = my_robot_interfaces::srv::InterPol2_Request;
  using Response = my_robot_interfaces::srv::InterPol2_Response;
};

}  // namespace srv

}  // namespace my_robot_interfaces

#endif  // MY_ROBOT_INTERFACES__SRV__DETAIL__INTER_POL2__STRUCT_HPP_
