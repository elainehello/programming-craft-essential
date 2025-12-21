package com.elainehello.loginsystem.api.auth;

import com.elainehello.loginsystem.service.auth.SessionService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.Parameter;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.responses.ApiResponses;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestHeader;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/v1/auth")
@Tag(name = "Authentication", description = "User authentication and registration endpoints")
public class LogoutController {

    private final SessionService sessionService;

    // initialize property/attribute
    public LogoutController(SessionService sessionService) {
        this.sessionService = sessionService;
    }

    @PostMapping("/logout")
    @Operation(summary = "User logout", description = "Invalidates the user session token")
    @ApiResponses(value = {
            @ApiResponse(responseCode = "200", description = "Logout successful"),
            @ApiResponse(responseCode = "400", description = "Invalid token")
    })
    public ResponseEntity<Void> logout(
            @Parameter(description = "Bearer token", required = true)
            @RequestHeader("Authorization") String authHeader) {
        try {
            // Extract token from "Bearer <token>"
            String token = authHeader.replace("Bearer ", "");
            sessionService.invalidateToken(token);
            return ResponseEntity.ok().build();
        } catch (Exception e) {
            return ResponseEntity.badRequest().build();
        }
    }
}
