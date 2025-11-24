package com.elainehello.ManagementSystem.controller;

import com.elainehello.ManagementSystem.model.entity.User;
import com.elainehello.ManagementSystem.service.UserService;
import io.swagger.v3.oas.annotations.Operation;
import org.springframework.web.bind.annotation.PostMapping;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Optional;
import java.util.List;

@Tag(name = "User API", description = "Operations for managing users")
@RestController
@RequestMapping("/users")
public class UserController {

    private final UserService userService;

    public UserController(UserService userService) {
        this.userService = userService;
    }

    // CREATE a user
    @Operation(summary = "Create a new user")
    @PostMapping
    public ResponseEntity<User> createUser(@RequestBody User user) {
        User savedUser = userService.saveUser(user);
        return ResponseEntity.ok(savedUser);
    }

    // GET a user by ID
    @Operation(summary = "Get a user by ID")
    @GetMapping("/{id}")
    public ResponseEntity<User> getUserById(@PathVariable Long id) {
        Optional<User> user = userService.getUserById(id);
        return user.map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    // GET a user by Email
    @Operation(summary = "Get a user by Email")
    @GetMapping("/email")
    public ResponseEntity<User> getUserByEmail(@RequestParam String email) {
        Optional<User> user = userService.getUserByEmail(email);
        return user.map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    // GET all users
    @Operation(summary = "Get all users")
    @GetMapping
    public ResponseEntity<List<User>> getAllUsers() {
        List<User> users = userService.getAllUsers();
        return ResponseEntity.ok(users);
    }

    // GET users by first name
    @Operation(summary = "Get users by first name")
    @GetMapping("/firstname/{firstName}")
    public ResponseEntity<List<User>> getUsersByFirstName(@PathVariable String firstName) {
        List<User> users = userService.getUsersByFirstName(firstName);
        return ResponseEntity.ok(users);
    }

    // GET user by last name
    @Operation(summary = "Get users by last name")
    @GetMapping("/lastname/{lastName}")
    public ResponseEntity<List<User>> getUsersByLastName(@PathVariable String lastName) {
        List<User> users = userService.getUsersByLastName(lastName);
        return ResponseEntity.ok(users);
    }

    // GET users by full name
    @Operation(summary = "Get users by full name")
    @GetMapping("/search")
    public ResponseEntity<List<User>> getUsersByFullName(
            @RequestParam(required = false) String firstName,
            @RequestParam(required = false) String lastName) {
        List<User> users = userService.getUsersByFullName(firstName, lastName);
        return ResponseEntity.ok(users);
    }

    // DELETE user by ID
    @Operation(summary = "Delete user by ID")
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteUserById(@PathVariable Long id) {
        userService.deleteUserById(id);
        return ResponseEntity.noContent().build();
    }
}
