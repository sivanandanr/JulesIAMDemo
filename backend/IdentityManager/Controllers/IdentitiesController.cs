using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using IdentityManager.Data;
using IdentityManager.Models;

namespace IdentityManager.Controllers;

[ApiController]
[Route("api/[controller]")]
public class IdentitiesController : ControllerBase
{
    private readonly AppDbContext _context;

    public IdentitiesController(AppDbContext context)
    {
        _context = context;
    }

    [HttpGet]
    public async Task<ActionResult<IEnumerable<UserIdentity>>> GetIdentities()
    {
        return await _context.Identities
            .Include(i => i.Roles)
            .ToListAsync();
    }

    [HttpGet("{id}")]
    public async Task<ActionResult<UserIdentity>> GetIdentity(int id)
    {
        var identity = await _context.Identities
            .Include(i => i.Roles)
            .ThenInclude(r => r.Entitlements)
            .FirstOrDefaultAsync(i => i.Id == id);

        if (identity == null) return NotFound();
        return identity;
    }

    [HttpPut("{id}/status")]
    public async Task<IActionResult> UpdateStatus(int id, [FromBody] string status)
    {
        var identity = await _context.Identities.FindAsync(id);
        if (identity == null) return NotFound();

        identity.Status = status;
        await _context.SaveChangesAsync();

        return NoContent();
    }
}
