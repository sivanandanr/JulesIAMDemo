using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using IdentityManager.Data;
using IdentityManager.Models;

namespace IdentityManager.Controllers;

[ApiController]
[Route("api/[controller]")]
public class AccessRequestsController : ControllerBase
{
    private readonly AppDbContext _context;

    public AccessRequestsController(AppDbContext context)
    {
        _context = context;
    }

    [HttpGet]
    public async Task<ActionResult<IEnumerable<AccessRequest>>> GetRequests()
    {
        return await _context.AccessRequests.OrderByDescending(r => r.CreatedAt).ToListAsync();
    }

    [HttpPost]
    public async Task<ActionResult<AccessRequest>> CreateRequest(AccessRequest request)
    {
        request.CreatedAt = DateTime.UtcNow;
        request.Status = "Pending";

        _context.AccessRequests.Add(request);
        await _context.SaveChangesAsync();

        return Ok(request);
    }

    [HttpPut("{id}/approve")]
    public async Task<IActionResult> ApproveRequest(int id)
    {
        var request = await _context.AccessRequests.FindAsync(id);
        if (request == null) return NotFound();

        request.Status = "Approved";

        // Logic to actually grant the access
        if (request.RequestType == "Role")
        {
            var identity = await _context.Identities.Include(i => i.Roles).FirstOrDefaultAsync(i => i.Id == request.IdentityId);
            var role = await _context.Roles.FindAsync(request.TargetId);
            if (identity != null && role != null && !identity.Roles.Any(r => r.Id == role.Id))
            {
                identity.Roles.Add(role);
            }
        }

        await _context.SaveChangesAsync();
        return NoContent();
    }

    [HttpPut("{id}/reject")]
    public async Task<IActionResult> RejectRequest(int id)
    {
        var request = await _context.AccessRequests.FindAsync(id);
        if (request == null) return NotFound();

        request.Status = "Rejected";
        await _context.SaveChangesAsync();
        return NoContent();
    }
}
