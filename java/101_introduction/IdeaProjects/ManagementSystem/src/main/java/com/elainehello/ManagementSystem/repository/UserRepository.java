package com.elainehello.ManagementSystem.repository;

import com.elainehello.ManagementSystem.model.entity.User;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.*;

@Repository
public interface UserRepository extends JpaRepository<User, Long> {

    // Find user by email (returns 'Optional' to avoid NullPointerException)
    Optional<User> findByEmail(String email);

    // Find --all users with a given first name (returns List<User>)
    List<User> findByFirstName(String firstName);

    // Find --all users with a given last name (returns List<User>)
    List<User> findByLastName(String lastName);

    // Find users by full name (returns List<User>)
    List<User> findByFirstNameAndLastName(String firstName, String lastName);

    // Delete a user by ID
    void deleteById(Long id);

    // Delete a user by email (void type)
    void deleteByEmail(String email);

}
