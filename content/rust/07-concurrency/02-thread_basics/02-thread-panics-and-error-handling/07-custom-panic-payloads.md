## Custom Panic Payloads

Can you panic with custom types, and what are the requirements?

---

Yes, you can panic with any type that implements Send. Example: panic!(CustomError { code: 42, message: "failed" }). The type must be Send because the panic payload crosses thread boundaries when join() returns it. You extract custom payloads using downcast_ref::<CustomType>(). This is useful for structured error information beyond simple strings.

