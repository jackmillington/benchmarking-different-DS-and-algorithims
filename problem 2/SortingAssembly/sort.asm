; Insertion Sort in ARM64 Assembly for macOS
; Compile with:
; clang -arch arm64 insertion_sort.s -o insertion_sort

.section __DATA,__data
.align 4
array_size:   .quad   10000        ; Size of array to sort
.align 4
array_start:  .zero   40000        ; Space for array (max 10000 integers)

; Format strings for output
start_msg:    .asciz  "Sorting array of size: %d\n"
time_msg:     .asciz  "Sorting took %lld nanoseconds\n"

.section __TEXT,__text
.globl _main
.align 2

_main:
    ; Preserve frame pointer
    stp x29, x30, [sp, #-16]!
    mov x29, sp

    ; Seed random number generator
    bl _arc4random_stir

    ; Generate random array
    mov x12, x0                  ; array size
    mov x13, #0                  ; loop counter

generate_loop:
    bl _arc4random               ; get random number
    and w14, w14, #0x3FFF        ; limit to 0-16383
    str w14, [x19, x13, lsl #2]  ; store in array
    add x13, x13, #1
    cmp x13, x12
    blt generate_loop

    ; Get start time
    sub sp, sp, #16
    mov x0, #0                   ; CLOCK_REALTIME
    mov x1, sp
    bl _clock_gettime

    ; Insertion Sort implementation
    mov x15, #1                  ; i = 1 (outer loop counter)

outer_loop:
    cmp x15, x12                 ; compare i with array size
    bge sort_done

    ; Load key (arr[i])
    lsl x16, x15, #2             ; multiply index by 4 for byte offset
    ldr w17, [x19, x16]          ; w17 = key = arr[i]
    
    ; j = i - 1
    sub x18, x15, #1             ; j = i - 1

inner_loop:
    cmp x18, #0                  ; while j >= 0
    blt inner_loop_done

    ; Load arr[j]
    lsl x20, x18, #2             ; multiply j by 4 for byte offset
    ldr w21, [x19, x20]          ; w21 = arr[j]

    ; Compare arr[j] with key
    cmp w21, w17
    ble inner_loop_done

    ; arr[j+1] = arr[j]
    add x22, x18, #1
    lsl x22, x22, #2
    str w21, [x19, x22]

    ; j--
    sub x18, x18, #1
    b inner_loop

inner_loop_done:
    ; arr[j+1] = key
    add x22, x18, #1
    lsl x22, x22, #2
    str w17, [x19, x22]

    ; i++
    add x15, x15, #1
    b outer_loop

sort_done:
    ; Get end time
    sub sp, sp, #16
    mov x0, #0                   ; CLOCK_REALTIME
    mov x1, sp
    bl _clock_gettime

    ; Calculate time difference (nanoseconds)
    ; Load seconds and nanoseconds into x0 and x1
    ldp x0, x1, [sp]             ; seconds, nanoseconds

    ; Convert seconds to nanoseconds and add to nanoseconds
    mov x2, #1000000000          ; Nanoseconds per second
    mul x0, x0, x2               ; Multiply seconds by 1 billion (nanoseconds per second)
    add x0, x0, x1               ; Add remaining nanoseconds to the result

    ; Print time
    adrp x1, time_msg@PAGE
    add x1, x1, time_msg@PAGEOFF
    bl _printf

    ; Exit
    mov x0, #0
    ldp x29, x30, [sp], #16
    ret
