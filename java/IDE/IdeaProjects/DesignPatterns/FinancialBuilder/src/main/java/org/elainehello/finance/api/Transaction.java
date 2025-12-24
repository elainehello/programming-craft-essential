package org.elainehello.finance.api;

import java.time.LocalDate;
import java.math.BigDecimal;
/*
*   DTO (Data Transfer Object) that carries the raw data from
*   your database
* */
public record Transaction(LocalDate date, String description, BigDecimal amount) {

}
