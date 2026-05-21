using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using IdentityManager.Data;
using IdentityManager.Models;

namespace IdentityManager.Controllers;

[ApiController]
[Route("api/[controller]")]
public class SourcesController : ControllerBase
{
    private readonly AppDbContext _context;

    public SourcesController(AppDbContext context)
    {
        _context = context;
    }

    [HttpGet]
    public async Task<ActionResult<IEnumerable<Application>>> GetSources()
    {
        return await _context.Applications.Where(a => a.IsTrustedSource).ToListAsync();
    }

    [HttpPost("{id}/aggregate")]
    public async Task<IActionResult> AggregateSource(int id)
    {
        var app = await _context.Applications.FindAsync(id);
        if (app == null) return NotFound();

        // Simulate HRMS Aggregation Logic
        // In a real app, this would call the connector to fetch data

        // Mocking a new identity found during aggregation
        var newUser = new UserIdentity
        {
            Username = "bwayne",
            DisplayName = "Bruce Wayne",
            Email = "bruce.wayne@example.com",
            Department = "Executive",
            JobTitle = "CEO",
            Status = "Active"
        };

        if (!await _context.Identities.AnyAsync(i => i.Username == newUser.Username))
        {
            _context.Identities.Add(newUser);
            await _context.SaveChangesAsync();
        }

        return Ok(new { message = "Aggregation successful", identitiesProcessed = 1 });
    }
}
